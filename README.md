A package for SublimeText3, see the [API documentation](https://www.sublimetext.com/docs/3/api_reference.html) for more information.

## what does it do
It allows you to scroll through the headers you manually defined in your code. Useful for longer scripts where you don't have clear boundaries within your code (for example, functions or classes).

## how to use
Use the command "Scroll through headers" in your Command Palette (default key is ctrl+shift+p). Scroll through the headers with up / down and the view will be automatically scrolled through.

Edit the provided .sublime-settings file to set how you defined your headers and how to strip the decorations and get to the header title itself.

I define my headers as below using a snippet as described [here](https://coderwall.com/p/remcca/text-header-snippet-for-sublime-text).

```
###########
# a header
###########
```
