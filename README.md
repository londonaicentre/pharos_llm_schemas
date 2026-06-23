### Repo to share materials with KCL Pharos team

For testing only

#### Review guide for schemas:

(1) Does the schema capture all necessary information in the Pharos data model?

(2) Does the schema capture 90%+ of key information found in oncology focused radiology reports that might be of use to (a) future RWE studies (b) as labels to train vision models?

(3) Do the Enums:

- offer comprehensive coverage with respect to (1) and (2)
- offer mutual exclusivity where only a single value is allowed (i.e. they do not 'clash' in any cases where an LLM may hover between multiple values)
- handle diverse cases for different cancer types, including outside of lung and breast?

(4) Are there edge cases or rare cases where the schema may struggle to precisely capture information?

(5) When testing with publicly available LLMs, are there specific cases where the LLM gets it wrong?

#### How to test in Claude / ChatGPT (web)

(1) `prompt_main.txt` contains the full prompt, including the schema. Paste it as the system prompt (e.g. in Claude, a Project's custom instructions)

(2) In the next message, paste a radiology report. Use this step to test different cases.

(3) The model should return JSON in `<output></output>` tags.

Only one report per chat - start a fresh chat between reports. Use the strongest available model.

