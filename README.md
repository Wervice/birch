<h1 align="center"> Birch </h1>
<h2 align="center"> One uniform logger for many languages </h2>

## Ussage

1. Include birch into your code
    a) Copy contents from birch file into your code
    b) Require/Include/Import... birch file in your code
2. Define variables

|Variable Name|Description|Example value|
|-------------|-----------|-------------|
|birch_path|Path to the log file to write into|`"../birch.log"`|
|birch_verbose|Enable verbose logging messages|false|
3. Call birch function
Birch provides one new function: `birch(level, message)`   
You have to pass a level and a message to the function.   
Supported levels are:

|Short level name|Level name|Level number|Level letter|
|----------|----------------|------------|------------|
|verbo|verbose|0|V|
|succ|success|1|S|
|warn|warning|2|W|
|erro|error|3|E|
|fata|fatal|4|F|

You can now simply read the log file or look for logs in the terminal.   
Every log entry will be built like this:
`[LEVEL] HH:MM:SS:MS mm/dd/YY | Message`

## Examples
```javascript
// JavaScript

const birch_path = "./.log"
const birch_verbose = true
eval(fs.readFileSync("birch.mjs").toString("ascii")) // Eval birch into project

birch("succ", "Start program");

birch("warn", "There is not much in this program")

```
