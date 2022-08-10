$uri = 'servibus/queue-name/messages?timeout=60 HTTP/1.1'
$releaseName = $env:RELEASE_RELEASENAME
$releaseWebUrl = $env:RELEASE_RELEASEWEBURL


$body = @{
  "param1": $releaseName,
  "param2": $releaseWebUrl
}

Write-Host 'some variable'

$headers = @{
'Authorization' = 'SAS',
'Content-Type': 'application/atom+xml;type=entry;charset=utf-8'
}


Invoke-RestMethod -Uri $uri -Headers 