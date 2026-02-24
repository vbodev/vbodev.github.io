$root = 'd:\Work\Sites\vbodev.github.io\content'
$fixed = 0
$skipped = 0

Get-ChildItem -Path $root -Include '*.md' -Recurse | ForEach-Object {
    $f = $_
    $rel = $f.FullName.Substring($root.Length + 1)

    # Only process ru/en/de language folders
    if ($rel -notmatch '^(ru|en|de).') {
        $skipped++
        return
    }

    $text = [System.IO.File]::ReadAllText($f.FullName, [System.Text.UTF8Encoding]::new($false))

    # Find the |RU]] link in the nav line
    if ($text -match '\[\[([^\]\|]+)\|RU\]\]') {
        $current = $matches[1]

        # Skip if already a full ru/ path
        if ($current -like 'ru/*') {
            $skipped++
            return
        }

        # Build correct ru/ path from this file's location
        $ruPath = $rel -replace '^(ru|en|de)[\\\/]', 'ru/'
        $ruPath = $ruPath -replace '\.md$', ''
        $ruPath = $ruPath -replace '\\', '/'

        $old = '[[' + $current + '|RU]]'
        $new = '[[' + $ruPath + '|RU]]'

        if ($text.Contains($old)) {
            $newText = $text.Replace($old, $new)
            [System.IO.File]::WriteAllText($f.FullName, $newText, [System.Text.UTF8Encoding]::new($false))
            Write-Host ('FIXED: ' + ($rel -replace '\\', '/'))
            $fixed++
        } else {
            $skipped++
        }
    } else {
        $skipped++
    }
}

Write-Host ""
Write-Host "Done. Fixed: $fixed  Skipped: $skipped"
