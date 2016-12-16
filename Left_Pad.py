#You know what, left pad is javascript package and referenced by React: 
#https://github.com/stevemao/left-pad
#One day his author unpublished it, then a lot of javascript projects in the world broken.
#You can see from github it's only 11 lines.
#You job is to implement the left pad function. If you do not know what left pad does, see examples below and guess.

#Example
#leftpad("foo", 5)
#>> "  foo"

#leftpad("foobar", 6)
#>> "foobar"

#leftpad("1", 2, "0")
#>> "01"

class StringUtils:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        return padChar * (size - len(originalStr)) + originalStr
