# Research

## Link format

### Extension

.lf - link fragments

### .lf file general requirements

Make it as UNIX way as possible

Possible separators:
- Space - more UNIX way format
- Comma, etc.

/home/andrey/Sources/experiments/ProjectExplorer/test/test_content -b "test_context_begin" -e test_context_end

### .lf file format

lf -e <file> -b <begin> -e <end>
```
lf [options] [file_path] [-b <begin_text>] [-e <end_text>]

Options:
-I include begin_text (default)
-i include end_text (default)
-E exclude begin_text
-e exclude end_text

Parameters:
-l [line_number] - scroll to line
```

## Fragment Linker

test_context_begin

Hello

test_context_end


