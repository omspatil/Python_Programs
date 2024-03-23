"""Write individual functions to obtain following expected outputs. Every function accepts a dictionary as 
parameter and returns resulting dictionary.
inverts {key:value} pairs
passed dictionary: {"key1":"value1", "key2":"value2", "key3":"value3"}
should return : {“value1”: “key1”, “value2”:“key2”, “value3”:“key3” }
returns collective values as list_elements:
passed dictionary: {"key1":"value1", "key2":"value2", "key3":"value3"}
should return: {"key1":[value1,value2,value3], "key2":[value1,value2,value3], 
"key3":[value1,value2,value3] }
returns collective values as list_elements, except own value:
passed dictionary: {"key1":"value1", "key2":"value2", "key3":"value3"}
should return : {"key1":[value2,value3], "key2":[value1,value3], "key3":[value1,value2] }
"""