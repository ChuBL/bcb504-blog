# bcb504-blog

## Website
 [My first blog](https://chubl.github.io/bcb504-blog/)

## Issues
### First update
<del>I have tried to rename the upper left button's text from My_first_blog while resulted in vain. 

<del>The attribute of `website: title` in `_quarto.yml` seems has nothing to do with the text in that button.

### Second update
Well, the actual issue is that no change has been made, no matter how many times I edit the `.qmd` file and hit the render button. I fixed this issue by manually closing all the file tabs in my Rstudio and then rendering the `index.qmd` for one more time.

I believe there are some background sessions hidden behind the Rstudio ui. I think that's why Rstudio and R language are not my favorite coding options.

### Third update
Now you can tell the difference I was talking about. The rendered website based on the `docs` directory remaining at the old version.
And if you clone the whole repository and render the `index.qmd` from the root directory, you can see the text in the upper left button has been changed from `My_first_blog` to `My first blog`.
The reason to this difference is still mystic to me.
