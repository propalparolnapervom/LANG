
# OPERATORS

## Conditional operators

### Ternary operator

[Docs](http://docs.groovy-lang.org/docs/groovy-2.5.0-beta-1/html/documentation/#_ternary_operator)

It allows do not use this
```
if (string!=null && string.length()>0) {
    result = 'Found'
} else {
    result = 'Not found'
}
```

but use this 
```
result = (string!=null && string.length()>0) ? 'Found' : 'Not found'
```
or even this
```
result = string ? 'Found' : 'Not found'
```

### Elvis operator

[Docs](http://docs.groovy-lang.org/docs/groovy-2.5.0-beta-1/html/documentation/#_elvis_operator)

It allows to do not repeat the name of the variable.

So this 
```
displayName = user.name ? user.name : 'Anonymous'   
```
may be written as this

```  
displayName = user.name ?: 'Anonymous' 
```

## Object operators

## Safe navigation operator
[Docs](http://docs.groovy-lang.org/docs/groovy-2.5.0-beta-1/html/documentation/#_safe_navigation_operator)

The Safe Navigation operator is used to avoid a `NullPointerException`. 
Typically when you have a reference to an object you might need to verify that it is not `null` before accessing methods or properties of the object. 
To avoid this, the safe navigation operator will simply return `null` instead of throwing an exception, like so:

```
# `find` will return a `null` instance
def person = Person.find { it.id == 123 } 

# use of the null-safe operator prevents from a `NullPointerException`
def name = person?.name      

# result is `null`
assert name == null  
```

