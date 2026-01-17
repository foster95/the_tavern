# the_tavern

*Welcome adventurer!*

The Tavern is an online e-commerce website store, designed for the Dungeons and Dragons and TTRPG community. The Tavern is B2C (Business to Consumer) one stop shop for all accessories needed for the table - from dice to rollers and bags, and is based within the UK, shipping globally. The Tavern features a user-friendly interface, secure payment system and allows for a seamless shopping experience. Within the website, customers will be able to browse products, read and understand product details and leave reviews for products. 

# Table of Contents
1. [UX](#ux)
    * [Five Planes of UX Design](#five-planes-of-ux-design)
        * [Strategy](#strategy)
        * [Scope](#scope)
        * [Structure](#structure)
        * [Skeleton](#skeleton)
        * [Surface](#surface)
2. [Development using Agile Methodology](#developing-using-agile-methodology)
    * [Epics](#epics)
        * [Products](#products)
        * [User Account and Authentication](#user-account-and-authentication)
        * [Shopping Bag and Checkout](#shopping-bag-and-checkout)
        * [Brand Experience](#brand-experience)
    * [User Stories](#user-stories)
        * [Products](#products-1)
        * [User Account and Authentication](#user-account-and-authentication-1)
        * [Shopping Bag and Checkout](#shopping-bag-and-checkout-1)
        * [Brand Experience](#brand-experience-1)

## UX
### Five Planes of UX Design
To guide the initial development stages of The Tavern, I used the theory of the 5 planes of UX - strategy, scope, structure, skeleton and surface.

### Strategy
#### Purpose
* The Tavern is a one stop shop allowing D&D and TTPG fans to purchase items that will enhance their table experience. The Tavern should be integrated with Stripe to allow for a secure and seamless payment experience
* The Tavern should also have a email newsletter, to help create a community within the TTRPG space. 
* The website should allow the team behind the tavern to add products, amend products and delete products as demand. 
* The Django admin for the website should allow the team behind The Tavern to keep track of orders
* A further fleshed out version of this project would use additional marketing tools would allow the team at The Tavern to understand items that are most popular and least popular so that they can help understand inventory requirements. 

#### Primary User Needs
* The Tavern staff need to be able to add, amend and delete products from the catalogue 
* The Tavern staff need to be able to track and amend incoming orders.
* User need to be able to browse products, add them to a shopping bag and complete their purchase securely
* Users should be able to sign up to The Tavern's community newsletter
* Users should be able to contact The Tavern to ask questions
* Users should be able to sign up to be a registered user
* Registered users should be able to see their own profile with shipping details which they can update and amend. 
* Registered users should be able to see their past orders 


#### Business Goals
* To provide a website that gives a fun, theatrical experience with aesthetics expected for the D&D/TTPG community
* The website should have an administrative portal that allows The Tavern's staff to track, amend and delete orders as required, as well as update the product inventory
* The website should have front end functionality to allow registered staff to login and make amendements to the catalog without having to log into the Django administration panel. 
* The website should streamline the purchasing process for both customers and staff.

### Scope
#### Functional Specifications
* Users will be able to see The Tavern's about page, informing customers about the history of the company 
* Users will be able to contact the team to ask questions
* Users will be able to browse products, add them to a shopping bag and purchase securely through Stripe
* Users will be able to create an account to become a registered user
* Registered users will be able to update their profile details
* Registered users will be able to see previous orders
* Super admins will be able to add or delete any user
* General staff will be able to see all orders and amend and delete orders
* General staff will be able to add, amend and remove products

#### Content Requirements
* A favicon icon must be visible on desktop 
* A header must include a logo and navigation bar on desktop. For mobile users, this navigation bar should be collapsable and the logo does not need to be seen
* A footer must include contact details, FAQ, shipping details, privacy policies. For desktop users the newsletter subscribe form should be visible in the footer. 
* The index page will have a hero image
* Product images will be seen throughout the website, along with product details
Users should be recieve messages to let them know of any state changes. These messages should fade after 4 seconds but also have a X to manually close the message. 
* Registered Users should be able to identify when they have logged in
* A customised 404 page for when users end up off the main site landscape
* Users should recieve an email after their order has been paid for and recieved which is tailored to The Tavern's branding guidelines. 

### Structure
#### Information Architecture 
The navigation bar should feature the following links: Home, Products (which should then be broken down into two categories: Dice, which is further split down into subcategories for the material of the dice, Table Accessories, All Products) and About. The profile and orders links should be available in a different section to the navigation bar. 

#### User Flow
| User | Function/Aim | Path
--- | --- | ---
User | Wishes to look for products | Home -> Products
User | Wishes to add products to shopping bag | Home -> Products -> Chosen Product -> Add to Bag
User | Wishes to make a purchase | Home -> Products -> Chosen Product -> Add to Bag -> Confirm purchase
User | Wishes to create an account | Home -> Sign Up
User | Wishes to login to account | Home -> Sign In
User | Wishes to see previous orders | Home -> Sign In -> Profile
User | Signs up to newsletter | Home -> Subscribe Form (mobile), Subscribe Form in footer (desktop)
Staff | Wants to add a product | Home -> Login -> Product Management -> Add a Product
Staff | Wants to amend a product | Home -> Login -> Product Management -> Amend a Product
Staff | Wants to delete a product | Home -> Login -> Product Management -> Delete Product

### Skeleton
#### Wireframes
I created a series of wireframes illustrating the mobile and desktop experience for users and staff. These wireframes were created with Canva

| Page | Mobile | Desktop
--- | --- | ---
Index | |
About | |
Products | |
Product Detail | |
Bag | |
Checkout | |
Order Confirmation ||
Sign In | |
Sign Up | |
Sign Out | |
Profile | |
Add Product | |
Amend a Product | |
Error 404 | |

### Surface
#### Colour Palette
As The Tavern is a website for TTRPG/D&D items, the website should have a rich, luxurious fantasy feel, similar to the aesthetics seen in games like Baldurs Gate and other D&D based games. I used coolors to help create the initial colour palette, which is focussed on this richness and warmth of an adventuring party, without leaning into the more cliche reds and golds that you often see associated with D&D and TTRPG games.

#### Typography
Using Our Own Thing's font matching extension, I settled on using Montserrat for the main body of the website, and Almendra for any headers. Montserrat is a standard font used across the industry, noted for its readability and simplicity. Almendra is a more decorative font which evokes the fantasy world, making it suited for The Tavern's aesthetics. Font Awesome was used for the social media icons in the footer. 

#### The Tavern's Logo/Wordmark

#### Development Using Agile Methodology
Using the Agile Methodology, I first created a set of epics, which then got broken down into 
a series of user stories to help understand down the requirements of the website. These user stories were all writen in the following formation: As a *Role* I can *Capability* so that *Receive Benefit*.

## Developing using Agile Methodology
### Epics
#### Products
* Users are able to browse all the products available 
* Users are able to learn the details of individual products, including materials and dimensions per item
* Users are able to view reviews of products
Registered users are able to leave reviews of products
* Users are able to see when they have put a product into their shopping bag
* Admin are able to add, remove and delete products
* Admin are able to keep product details up to date

#### User Account and Authentication
* Users are able to sign up to become registered users
* Users are able to recieve a confirmation email once they have completed a product purchase  §a
* Registered users are able to securely log in and log out of their account
* Registered users are able to manage their own personal details in their profile, including a profile picture
* Registered users are able to reset their password at any time
* Registered users are able to see past orders attached to their account

#### Shopping Bag and Checkout
* Users can add items to their shopping bag
* Users can choose the amount of individual products they want
* Users can increase and decrease quantity of the individual products
* Users can remove items from their shopping bag
* Users can securely enter their card details and complete the payment process
* Users are taken to an order confirmation page on succesful purchase

#### Brand Experience
* The website is themed around The Tavern's brand guidelines
* Every single product has a correct associated image attached
* Users are able to see the history of the brand 
* Photos used across the website are appropriately matched to the material 
* Users are able to contact the team behind The Tavern

### User Stories
#### Products
* As a user of the website, I want to be able to browse products so that I can find items to purchase
* As a user of the website, I want to be able to view product details for each individual product, so that I can understand if the product is suited for my needs
* As a user of the website, I want to be able to read product reviews, so that I can see how other people have experienced the item and decide if it suits my needs
* As a registered user of the website, I want to be able to leave product reviews, so that I can help inform other potential buyers about my opinion of the product
* As a staff member (Admin role), I want to be able to approve product reviews, so that I can ensure that only quality reviews end up on the website
* As a staff member (Admin role), I want to be able to delete product reviews, so that I can ensure that innapropriate reviews do not end up on the website
* As a staff member (Admin role), I want to be able to add, amend and delete products from the website 

#### User Account and Authentication
* As a user, I can sign up to become a registered user, so that I can track have a profile that tracks previous orders and automatically populate fields with my details at checkout
* As a user, I will recieve a confirmation email when I have created an account, so that I can securely validate my account
* As a registered user I am able to securely log in and log out of my profile so that I know that my account is safe
* As a registered user, I am able to update my profile information, so that I can be sure that my details are up to date
* As a registered user, I am able to give myself a profile picture, so that I can have a photo on my profile
* As a registered user, I am able to reset my password at any time, so that I can keep my account secure
* As a registered user, I am able to see my previous orders, so that I can track any orders I have made in the past. 

#### Shopping Bag and Checkout
* As a user of the website, I can add items to a shopping bag and see how much the grand total is, so that I can track how much I am spending
* As a user of the website, I can change the quantity of the items in my shopping bag and an updated grand total, so that I can track how much I am spending
* As a user of the website I can remove items from my shopping bag and see an updated grand total, so that I can remove items I do not need anymore
* As a user of the website I can be shown all the items I am buying, plus the subtotal, shipping details and grand total before I complete the purchase, so that I can decide that I definitely want to complete the purchase
* As a user of the website I can enter my details into the checkout securely, using the Stripe API, so that I can purchase items safely and securely
* As a user of the website, I can be shown my order details once my order is confirmed, so that I can see that my order has been completed
* As a user of the website, I can recieve an email confirming my order once my order has been succesfully submitted

#### Brand Experience
* As a user, I want to be able to sign up to The Tavern's newsletter, so I can learn about their community
* As a user, I want to be able to see information about the company, so I can know who I'm buying from
* As a user, I want to be able to contact the team behind The Tavern, so I can know that I can message directly with questions, queries or suggestions
* As a staff member (Admin role) I want to be able to update the information on the company, so that I can keep this up to date as the company grows and expands

### MoSCoW Prioritisation
Using the MoSCoW priotisation method, I then further broke down my user stories into four seperate categories. These categories are:
 
* Must Have - this should take up no more than 50% of the entire project. 
* Should Have
* Could Have
* Won't Have

Using GitHub's issue board, I grouped each user story by its category and then transferred these to the GitHub Projects kanban board which I used to track website progression over the remaining project

#### Must Have
* As a user of the website, I want to be able to browse products so that I can find items to purchase
* As a user of the website, I want to be able to view product details for each individual product, so that I can understand if the product is suited for my needs
* As a staff member (Admin role), I want to be able to add, amend and delete products from the website
* As a user, I can sign up to become a registered user, so that I can track have a profile that tracks previous orders and automatically populate fields with my details at checkout
* As a user, I will recieve a confirmation email when I have created an account, so that I can securely validate my account
* As a registered user I am able to securely log in and log out of my profile so that I know that my account is safe
* As a user of the website, I can add items to a shopping bag and see how much the grand total is, so that I can track how much I am spending
* As a user of the website, I can change the quantity of the items in my shopping bag and an updated grand total, so that I can track how much I am spending
* As a user of the website I can remove items from my shopping bag and see an updated grand total, so that I can remove items I do not need anymore
* As a user of the website I can be shown all the items I am buying, plus the subtotal, shipping details and grand total before I complete the purchase, so that I can decide that I definitely want to complete the purchase
* As a user of the website I can enter my details into the checkout securely, using the Stripe API, so that I can purchase items safely and securely
* As a user, I want to be able to sign up to The Tavern's newsletter, so I can learn about their community

#### Should Have
* As a user of the website, I want to be able to read product reviews, so that I can see how other people have experienced the item and decide if it suits my needs
* As a registered user of the website, I want to be able to leave product reviews, so that I can help inform other potential buyers about my opinion of the product
* As a staff member (Admin role), I want to be able to approve product reviews, so that I can ensure that only quality reviews end up on the website
* As a staff member (Admin role), I want to be able to delete product reviews, so that I can ensure that innapropriate reviews do not end up on the website
* As a registered user, I am able to update my profile information, so that I can be sure that my details are up to date
* As a registered user, I am able to reset my password at any time, so that I can keep my account secure
* As a registered user, I am able to see my previous orders, so that I can track any orders I have made in the past.
* As a user of the website, I can be shown my order details once my order is confirmed, so that I can see that my order has been completed
* As a user of the website, I can recieve an email confirming my order once my order has been succesfully submitted
* As a user, I want to be able to contact the team behind The Tavern, so I can know that I can message directly with questions, queries or suggestions

#### Could Have
* As a registered user, I am able to give myself a profile picture, so that I can have a photo on my profile
* As a user, I want to be able to see information about the company, so I can know who I'm buying from
* As a staff member (Admin role) I want to be able to update the information on the company, so that I can keep this up to date as the company grows and expands

## Web Marketing
### Keyword and SEO research
At the beginning of the project, I sat down and documented all of the keywords associated with The Tavern, in order to try and improve my SEO rating as much as possible. To start this process, I began by noting down all the general keywords associated with my website:

* Dungeons and Dragons
* D&D
* TTRPG
* D20
* Dice
* Dnd Dice
* TTRPG Dice
* Dungeon and Dragons gifts

Next, I drilled these down into more specific long and short tail keywords:

* D&D
* D&D Dice
* Dungeons and Dragons
* Dimension 20
* Critical Role
* TTRPG
* TTRPG Dice
* Gift ideas for D&D fans
* Gift ideas for Dimension 20 fans
* Gift ideas for Critical Role fans
* Gift ideas for TTRPG fans
* Dice roller
* Dice bag
* Resin dice
* Acrylic dice
* Gemstone dice
* D&D accessories
* TTRPG accessories
* Best TTRPG dice

I also used Googles search bar to help me find related search phrases that users could be looking for, and I also used wordtracker.com to complete two free searches to find similar competition keywords at the time of searching. 

IMAGES FROM GOOGLE SEARCHES GO HERE

After further consideration, I removed a number of these long and short tail keywords as they were either too competitive or would be too general for my purposes. My final list therefore became the following:

* D&D
* D&D Dice
* Dungeons and Dragons
* TTRPG
* TTRPG Dice
* Gift ideas for D&D fans
* Gift ideas for TTRPG fans
* Dice roller
* Dice bag
* Resin dice
* Acrylic dice
* Gemstone dice
* D&D accessories
* TTRPG accessories
* Best TTRPG dice
* Best Dnd Dice

Following this, I developed a content strategy which would help me align my requirements with the project I built:

#### User Requirements
* High quality, accurate product information
* Clear pricing details
* Easy navigation and search functionality to find specific products
* Secure and straightforward checkout process
* Fast answers to standard questions
* Ability to sign up to a mailing list

#### Content
* Detailed product descriptions, highlighting the item, the materials it is made from, product dimensions and within the product page
* Clear product categories and filters to help users find products quickly and easily based on their preferences
* Testimonials from previous happy customers
* Customer support content including FAQs, shipping info and return policies information
* Clear sign posted opportunities to sign up to the mailing list

#### Internal linking
* Category pages linking to individual product pages
* Navigation links to category pages
* Footer links to important information such as FAQs and contact information
* 404 page for broken pages

#### Marketing Strategies
As part of the building the website, I considered what The Tavern would use for marketing techniques, and came up with the following:

#### Who?
The Tavern's primary users are people who are already enganging with TTRPG and D&D games, as the items they sell are for use at the table itself. These could be people who virtually play TTRPG/D&D but it is more likely that these are people who meet and play games in physical spaces and therefore have a need for dice, dice rollers and dice bags

#### What online platforms do they use?
TTRPG and D&D has a large presence online already, particularly on Instagram, Tik Tok and Discord. If they were focussing on paid for marketing/influencer marketing, I would suggest they focus on these platforms.

#### What do they need?
D&D and TTRPG players are typically looking for communities, as both games are really considered to just be elaborate storytelling told in groups of friends. Therefore I would focus any marketing on this aspect of community and togetherness, as well as sharing funny memes about D&D, TTRPG tips and tricks for the table, and other fun aspects such as lore from Baldurs Gate. 

#### Sales and Discounts? 
As The Tavern is a small business, I would only advocate that they do sales seasonally rather than all the time, or in line with important events within the D&D community that The Tavern could piggyback of, such as season finales of Dimension 20 or Critical Role. 

#### Goals of the Business
The ultimate goal of The Tavern is to sell D&D accessories, but also to build a community of D&D and TTRPG fans

#### Budget
The Tavern do have a small marketing budget, however I would personally suggest to them that the rely on organic marketing rather than paid for marketing. You can often find that it is the outsiders and the misfits that drift towards D&D and TTPRG and those people can be especially cynical and shrewd about paid for marketing. After all reputation takes a lifetime to build and seconds to shatter. 

## Tools and Technologies
### Media and Design
* Google Gemini - Product images
* Coolors - Colour Palettes
* Our Own Thing - Font pairing website
* Google Fonts - Fonts across the full website
* Canva - Wireframes

### Database
* Miro - ERD creation