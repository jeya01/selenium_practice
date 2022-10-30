'''
    XPATH is defined as XML path
    XPATH worrks with DOM not with HTML
    XPATH is a language/syntax used to locate the element in a webpage using XML path expression
    it is used to navigate through elements and attributes in DOM
    it is an address of an element

    Types
    1. Absolute / Full XPATH
    2. Relative / partial XPATH

    Difference
    Absolute XPATH starts from the root node /html but the relative XPATH starts directly from the element in the current node
    Absolute XPATH starts with / whereas relative xpath starts with //
    absolute xpath uses tags/nodes whereas relative xpath uses attriutes

//.. to immediate parent

    writing XPATH manually
    start from the last to first

    Relative xpath
    //tagname[@attribute='value']
    eg: //input[@id="small-searchterms"]
    if tag name is not known then specify * instead of tagname
    eg: //*[@id="small-searchterms"]

    Relative vs absolute XPATH, which is preferred and why?
    Relative XPATH is more reliable than absolute XPATH. Because when an element in dom misplaced then the absolute xpath wont
    return the element. and absolute xpath is very long as it starts from the root node where as relative xpath is specific to
    the particular element based on the tag's attribute and its value


    type 1: using and, or operators
    //input[@id="search_query_top" or @placeholder="Search"] --choose the element if either one condition match
    //input[@id="search_query_top" and @placeholder="Search"] --choose when both the conditions match

    type 2:Contains() and starts-with()
    Contains is used when the element attributes changed dynamically
    //*[contains(@id,"st")] here the contains look for the element which has common value here it first char st at the starting position
    //*[starts-with(@id,"st")] if the both the attriutes starts with st

    type3: text()
    //a[text()="text"]

    self -- current node is called self
    //a[contains(text(),'PVV Infra')]/self::a

    LOCATING ELEMENT BASED ON KNOWN ELEMENT
    self -- current node is called self

    parent -- the one above self is called parent
    child -- the one below the self
    ancestor -- parrent of parent
    desendent -- child of child/grand child
    following -- traverse all the elements that comes after current tag
    following sibling  -- traverse from the current tag to next sibling html tag
    preceeding -- traverse all the elements that comes before current tag
    following preceeding -- traverse from the current tag to previous sibling html tag



'''


'''1. Why do we need XPATH? Why not other locators?
other locators are sometimes available or duplicated except id(unique). if those options are not available 
then we go to either css selector or XPATH. 

2. Can we rely on browser plugins alone? 
When the content is dynamic, we need to try XPATH

3. What is XPATH?
XPATH - XML path - used to identify an element. most flexile and strongest location strategy used to identify an element

4. How XML PATH and its functions handle HTML elements ?
SGML - Standard Genealised Markup Language . it is the parent for both XML and HTML. with the help of parent XML is
able to read the HTML elements

5. Types of XPath.
Absolute and Relative

6. Identification strategies:
LOCATING THE ELEMENTS WITH RESPECT TO ELEMENTS AND ATTRIBUTES
       a) Locating Elements with Known Attribute
       //*[@attriute='value]  here * looks thro all the elements in the web page eg: //*[@name='txtUserName']
       b) Locating Elements with known Element and Attributes
       //input[@name='txtUserName']
       c) Locating Elements with Known Visible Text (exact match)
       //a[text()='OrangeHRM, Inc']
       d) Locating Elements when part of the visible text (partial match)
        //*[contains(text(),'OrangeHRM, Inc')]   
        e) Locating Elements with Multiple Attributes
        //*[@name='username'][@placeholder='Username']
       f) Locating elements when starting visible text is known
       //*[starts-with(@name,'user')]
       g) Locating Elements with Dynamic Attribute values
       //*[contains(text(),'OrangeHRM, Inc')] 
       //*[starts-with(@name,'user')]

    contains and starts-with not only for text and also for the other attriutes as well
       '''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
driver.maximize_window()

'''  self -- current node is called self'''
#t = driver.find_element(By.XPATH,"//a[contains(text(),'PVV Infra')]/self::a").text

'''parent -- the one above self os called parent'''
#t = driver.find_element(By.XPATH,"//a[contains(text(),'PVV Infra')]/parent::td").text

'''child -- the one below the self'''
'''because this has multiple child elements'''
#t = driver.find_elements(By.XPATH,"//a[contains(text(),'PVV Infra')]/ancestor::tr/child::td")

'''    ancestor -- parent of parent '''
#t = driver.find_element(By.XPATH,"//a[contains(text(),'PVV Infra')]/ancestor::tr").text

#desendent - - child of child / grand child
#t = driver.find_elements(By.XPATH,"//a[contains(text(),'Innocorp')]/ancestor::tr/descendant::*")

#print("no of nodes;",len(t))


# following - - traverse all the elements that comes after current tag
#followings = driver.find_elements(By.XPATH,"//a[contains(text(),'Innocorp')]/ancestor::tr/following::*")
#print("no of nodes;",len(followings))

# following siblings - traverse from the current tag to next child tag
#following_Sibling = driver.find_elements(By.XPATH,"//a[contains(text(),'Sai Capital')]/ancestor::tr/following-sibling::*")
# "*" prints all the elements that matches with the XPATH
#print("no of nodes;",len(following_Sibling))

#preceding
#precedings = driver.find_elements(By.XPATH,"//a[contains(text(),'Sai Capital')]/ancestor::tr/preceding::tr")
#print("no of nodes;",len(precedings))


precedingSiblings = driver.find_elements(By.XPATH,"//a[contains(text(),'Sai Capital')]/ancestor::tr/preceding-sibiling::tr")
print(len(precedingSiblings))

driver.close()