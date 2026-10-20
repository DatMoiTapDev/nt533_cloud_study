# Portable localhost server. Windows PowerShell 5.1 / .NET; no admin, no downloads.
$ErrorActionPreference = 'Stop'
$rootDir = [IO.Path]::GetFullPath($PSScriptRoot)
$portNumber = 18765
$baseUrl = "http://127.0.0.1:$portNumber/"
function Open-Study {
    $edgePath = $null
    foreach ($programDir in @(${env:ProgramFiles(x86)}, $env:ProgramFiles)) {
        if ($programDir) {
            $candidate = Join-Path $programDir 'Microsoft\Edge\Application\msedge.exe'
            if (Test-Path $candidate) { $edgePath=$candidate; break }
        }
    }
    if ($edgePath) { Start-Process -FilePath $edgePath -ArgumentList "--app=$baseUrl" }
    else { Start-Process $baseUrl }
}
$server = [Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback, $portNumber)
try { $server.Start() }
catch {
    try {
        $health = Invoke-WebRequest -UseBasicParsing -Uri ($baseUrl + 'cloudlab-health') -TimeoutSec 2
        if ($health.Content.Trim() -eq 'CloudLab-local-v1') { Open-Study; exit 0 }
    } catch {}
    Write-Host 'Port 18765 is busy. Close the other program or restart Windows, then try again.'
    exit 1
}
Write-Host ''
Write-Host 'CloudLab is running OFFLINE at http://127.0.0.1:18765/' -ForegroundColor Green
Write-Host 'Keep this window open while studying. Close it or press Ctrl+C to stop.'
Write-Host 'Progress is saved in your browser. Use Export backup before clearing browser data.'
Write-Host ''
Open-Study
$mime = @{'.html'='text/html; charset=utf-8'; '.js'='text/javascript; charset=utf-8'; '.css'='text/css; charset=utf-8'; '.json'='application/json; charset=utf-8'; '.pdf'='application/pdf'; '.csv'='text/csv; charset=utf-8'; '.md'='text/plain; charset=utf-8'; '.txt'='text/plain; charset=utf-8'; '.png'='image/png'; '.svg'='image/svg+xml'; '.ico'='image/x-icon'}
try {
 while ($true) {
    $client = $server.AcceptTcpClient()
    $client.ReceiveTimeout = 10000; $client.SendTimeout = 30000
    $stream = $client.GetStream()
    $fileStream=$null
    try {
        $reader = [IO.StreamReader]::new($stream, [Text.Encoding]::ASCII, $false, 4096, $true)
        $request = $reader.ReadLine()
        if (-not $request) { continue }
        $parts = $request.Split(' ')
        $method = $parts[0]
        $headers = @{}
        $headerBytes = 0
        while ($true) {
            $line = $reader.ReadLine()
            if ([string]::IsNullOrEmpty($line)) { break }
            $headerBytes += $line.Length
            if ($headerBytes -gt 32768) { throw 'Header too large' }
            $colon = $line.IndexOf(':')
            if ($colon -gt 0) { $headers[$line.Substring(0,$colon).ToLowerInvariant()]=$line.Substring($colon+1).Trim() }
        }
        $status='200 OK'; $type='text/plain; charset=utf-8'; $payload=$null; $fileStream=$null; $startByte=[long]0; $endByte=[long]0; $extra=''
        if ($parts.Length -lt 2 -or @('GET','HEAD') -notcontains $method) { $status='405 Method Not Allowed'; $payload=[Text.Encoding]::UTF8.GetBytes('GET/HEAD only.') }
        elseif ($headers.ContainsKey('host') -and $headers['host'] -notin @("127.0.0.1:$portNumber","localhost:$portNumber")) { $status='403 Forbidden'; $payload=[Text.Encoding]::UTF8.GetBytes('Local host only.') }
        elseif ($parts[1].Split('?')[0] -eq '/cloudlab-health') { $payload=[Text.Encoding]::UTF8.GetBytes('CloudLab-local-v1') }
        else {
            $target = [Uri]::UnescapeDataString($parts[1].Split('?')[0]).Replace('/',[IO.Path]::DirectorySeparatorChar)
            $relative = $target.TrimStart([IO.Path]::DirectorySeparatorChar)
            if (-not $relative) { $relative='index.html' }
            $full = [IO.Path]::GetFullPath((Join-Path $rootDir $relative))
            $allowed = $full.StartsWith($rootDir+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)
            if (-not $allowed) { $status='403 Forbidden'; $payload=[Text.Encoding]::UTF8.GetBytes('Forbidden') }
            elseif (-not [IO.File]::Exists($full)) { $status='404 Not Found'; $payload=[Text.Encoding]::UTF8.GetBytes('Not found') }
            else {
                $ext=[IO.Path]::GetExtension($full).ToLowerInvariant(); $type=$mime[$ext]
                if (-not $type) { $type='application/octet-stream' }
                $fileStream=[IO.File]::OpenRead($full); $endByte=$fileStream.Length-1
                $extra="Accept-Ranges: bytes`r`n"
                if ($headers.ContainsKey('range') -and $headers['range'] -match '^bytes=(\d*)-(\d*)$') {
                    $a=$Matches[1];$b=$Matches[2]
                    if ($a -ne '') { $startByte=[long]$a; if ($b -ne '') { $endByte=[Math]::Min([long]$b,$endByte) } }
                    elseif ($b -ne '') { $startByte=[Math]::Max([long]0,$fileStream.Length-[long]$b) }
                    if ($startByte -lt 0 -or $startByte -gt $endByte -or $startByte -ge $fileStream.Length) {
                        $status='416 Range Not Satisfiable';$extra="Content-Range: bytes */$($fileStream.Length)`r`n";$fileStream.Dispose();$fileStream=$null;$payload=[byte[]]@()
                    } else { $status='206 Partial Content'; $extra+="Content-Range: bytes $startByte-$endByte/$($fileStream.Length)`r`n" }
                }
            }
        }
        $length = if ($null -ne $fileStream) { [Math]::Max([long]0,$endByte-$startByte+1) } else { $payload.Length }
        $response="HTTP/1.1 $status`r`nContent-Type: $type`r`nContent-Length: $length`r`nCache-Control: no-store`r`nX-Content-Type-Options: nosniff`r`nConnection: close`r`n$extra`r`n"
        $head=[Text.Encoding]::ASCII.GetBytes($response);$stream.Write($head,0,$head.Length)
        if ($method -ne 'HEAD') {
            if ($null -ne $fileStream) {
                [void]$fileStream.Seek($startByte,[IO.SeekOrigin]::Begin)
                $buffer=New-Object byte[] 65536; $remaining=$length
                while ($remaining -gt 0) { $read=$fileStream.Read($buffer,0,[int][Math]::Min($buffer.Length,$remaining));if ($read -eq 0) { break };$stream.Write($buffer,0,$read);$remaining-=$read }
            } elseif ($payload.Length -gt 0) { $stream.Write($payload,0,$payload.Length) }
        }
    } catch { Write-Verbose $_.Exception.Message }
    finally { if ($null -ne $fileStream) { $fileStream.Dispose() };$stream.Dispose();$client.Close() }
 }
} finally { $server.Stop() }
