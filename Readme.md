# The Python Challenge

## 1

```ord()``` for translating characters into ascii

```chr()``` for translating ascii into characters

```int()``` for translating characters(like '1','2','3'...'99'...) into integer, and the base given will tell python how to interpret it

```"".join([])``` translate list to string

### base 10 to base 2

```bin(11)```

### base 2 to base 10

```int(str, 2)```

### base 10 to base 16

```hex(10)```

```print "%x"%16```

### base 16 to base 10

```int(str, 16)```

```0xff```

#### base 10 to base 8

``` print "%o", 9 ```

### base 8 to base 10

```int(str, 8)```

```011```


## 2

```set([])``` init a set

```{}.fromkeys([key,], init_value)``` init a dic with the offered key, and init the value with init_value 

```print,``` print without a new-line

## 3

### re

```m = search(pattern, string)```  search for all the strings matched, and it will be stored as groups, use like```m.group(0)``` to get them

```m = match(pattern, string)``` different from ```search()```, it will try to match from the beginning of the string.

```m = re.split(pattern, string)``` split the string according to the regular pattern, and all the sub-string splited will be sent to m, a list.

```m = re.findall(pattern, string)``` find all the sub-string matched, and send them to a list(m).

## 4
http://www.pythonchallenge.com/pc/def/linkedlist.html
