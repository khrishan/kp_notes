# CSS Notes

## Use Hyphens

**DO NOT** use camelCase when naming CSS identifiers.

Use hypens!

This is consistant with the CSS property names. As shown below : 

```css
#tower-of-pisa{
    font-style: italic;
}

```

## BEM Convention
```
B - Block 
E - Element (__)
M - Modifier (--)
```

Look at this stick-man. We can split the CSS of this stick-man using the BEM convention.

Consider the following : 
+ `stick-man` is the **Block**
+ `head` is the **Element**
+ `blue` is the **Modifier**

```css
.stick-man__head--small {
    width : 50%;
}

.stick-man__head--big {
    width : 200%;
}
```

## CSS & JS
Sometimes JS code relies on CSS class names.

If that is the case, put a `js-` prefix to the class name.

```html
<div class="site-navigation js-site-navigation">

</div>
```

## CSS Variables

CSS now finally supports variables.

They are **case sensitive**.

A CSS Variable is any 'property' whose name begines with two dashes.
```css
.test {
    color: #8cacea;
    --colour: blue;
}
```

### Scoping CSS Variables
Variable can have scopes, global or local.

```css
{
    /* :root allows you to target the highest level element in the DOM. */
    :root {  /* Global */
        --color: black;
    }
    .block { /* Local */
        color: #8cacea;
        --colour: blue; 
    }
}
```

### Using CSS Variables
You reference a variable by using the `var()` function.

You can also set `default` values.

```css
:root {
  --font-size: 20px;
}

.test {
  font-size: var(--font-size, 16px);
}
```

### `calc()`
If you want to do math, you need the CSS `calc()` function for that.

```css
.margin {
    --space: calc(20px * 2);
    font-size:  var(--space);  /*equals 40px*/
}
```

### Normal Inheritance rules apply
```css
div {
  --color: red;
}

div.test {
  color: var(--color);
}

div.ew {
  color: var(--color);
}
```

### How to change variables based in JS
```js
function handleThemeUpdate(e) {
  switch(e.target.value) {
    case 'dark': 
      root.style.setProperty('--bg', 'black');
      root.style.setProperty('--bg-text', 'white');
      break
    case 'calm': 
       root.style.setProperty('--bg', '#B3E5FC');
       root.style.setProperty('--bg-text', '#37474F');
      break
    case 'light':
      root.style.setProperty('--bg', 'white');
      root.style.setProperty('--bg-text', 'black');
      break
  }
}
```


## References
[https://medium.freecodecamp.org/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849](https://medium.freecodecamp.org/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849)

[http://getbem.com/naming/](http://getbem.com/naming/)

[https://medium.freecodecamp.org/learn-css-flexbox-in-5-minutes-b941f0affc34](https://medium.freecodecamp.org/learn-css-flexbox-in-5-minutes-b941f0affc34)