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
    * [MoSCoW Prioritisation](#moscow-prioritisation)
        * [MoSCoW summary](#moscow-summary) 
        * [Must Have](#must-have)
        * [Could Have](#could-have)
        * [Should Have](#should-have)
    * [Database Design](#databse-design)
    * [Website Features](#website-features)
    * [Testing](#testing)
        * [Summary of Testing](#summary-of-testing)
        * [Lighthouse](#lighthouse)
        * [HTML Testing](#html-testing)
        * [CSS Testing](#css-testing)
        * [WAVE/Aim Web Accessibility Testing](#wave-aimweb-accessibility-testing)
        * [PEP8 Testing](#pep8-testing)
        * [JShint Testing](#jshint-testing)
        * [Device Testing]
        * [Browser Testing]
        * [Manual Testing](#manual-testing)
        * [Automated Testing](#automated-testing)
        * [Testing Against User Stories](#testing-against-user-stories)
    * [Web Marketing](#web-marketing)
        * [Keywords and SEO Research](#keyword-and-seo-research)
        * [Marketing Strategies](#marketing-strategies)
    * [Deployment](#deployment)
    * [Tools and Technologies](#tools-and-technologies)
    * [Credits and Acknowledgments]
    * [A Final Word from the Developer]


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
Users should be receive messages to let them know of any state changes. These messages should fade after 4 seconds but also have a X to manually close the message. 
* Registered Users should be able to identify when they have logged in
* A customised 404 page for when users end up off the main site landscape
* Users should receive an email after their order has been paid for and received which is tailored to The Tavern's branding guidelines. 

### Structure
#### Information Architecture 
The navigation bar should feature the following links: Home, Products (which should then be broken down into two categories: Dice, which is further split down into subcategories for the material of the dice, Table Accessories, All Products) and About. The profile and orders links should be available in a different section to the navigation bar. 

#### User Flow
| User | Function/Aim | Path
--- | --- | ---
User | Wishes to look for products | Home → Products
User | Wishes to add products to shopping bag | Home → Products → Chosen Product → Add to Bag
User | Wishes to make a purchase | Home → Products → Chosen Product → Add to Bag → Confirm purchase
User | Wishes to create an account | Home → Sign Up
User | Wishes to login to account | Home → Sign In
User | Wishes to see previous orders | Home → Sign In → Profile
User | Signs up to newsletter | Home → Subscribe Form (mobile), Subscribe Form in footer (desktop)
Staff | Wants to add a product | Home → Login → Product Management → Add a Product
Staff | Wants to amend a product | Home → Login → Product Management → Amend a Product
Staff | Wants to delete a product | Home → Login → Product Management → Delete Product

### Skeleton
#### Wireframes
I created a series of wireframes illustrating the mobile and desktop experience for users and staff. These wireframes were created with Canva

| Page | Mobile | Desktop
--- | --- | ---
Index | ![Mobile - Index Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-index.png) | ![Desktop - Index Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-index.png)
About | ![Mobile - About Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-about.png) | ![Desktop - About Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-about.png)
Products | ![Mobile - Products](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-categories.png) | ![Desktop - Products Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-categories.png)
Product Detail | ![Mobile - Product Detail Wireframes](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-product-details.png) | ![Desktop - Product Detail Wireframes](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-product-detail.png)
Bag | ![Mobile - Bag Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-bag.png) | ![Desktop - Bag Wireframes](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-bag.png)
Checkout | ![Mobile - Checkout Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-checkout.png)| ![Desktop - Checkout Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-checkout.png)
Order Confirmation | ![Mobile - Order Confirmation](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-order-confirmation.png) | ![Desktop - Order Confirmation](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-order-confirmation.png)
Sign In | ![Mobile - Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-sign-in.png) | ![Desktop - Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-sign-in.png)
Sign Up | ![Mobile - Sign Up](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-sign-up.png) | ![Desktop - Sign Up](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-sign-up.png)
Sign Out | ![Mobile - Sign Out](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-sign-out.png) | ![Desktop - Sign Out](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-sign-out.png)
Profile | ![Mobile - Profile](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-profile.png) | ![Desktop - Profile](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-profile.png)
Add Product | ![Mobile - Add Product](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-add-product.png) | ![Desktop - Add Product Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-add-product.png)
Amend a Product | ![Mobile - Amend Product](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-amend-product.png) | ![Desktop - Amend Product Wireframe](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-amend-product.png)
Error 404 | ![Mobile - Error 404](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/mobile-error-404.png) | ![Desktop - Error 404](https://github.com/foster95/the_tavern/blob/main/documentation/wireframes/desktop-error-404.png)

### Surface
#### Colour Palette
As The Tavern is a website for TTRPG/D&D items, the website should have a rich, luxurious fantasy feel, similar to the aesthetics seen in games like Baldurs Gate and other D&D based games. I used coolors to help create the initial colour palette, which is focussed on this richness and warmth of an adventuring party, without leaning into the more cliche reds and golds that you often see associated with D&D and TTRPG games.

The initial colour palette created for The Tavern can be found below:

![Initial Colour Palette for The Tavern](https://github.com/foster95/the_tavern/blob/main/documentation/brand/initial-colour-palette.png)

At the end of the devlopment of the website I undertook WAVE testing, which raised contrast issues with the current colour palette. With that in mind, the primary accent was tweaked slightly to make it darker and pass the AIM minimum checker, whilst still keeping the original colour palette in mind. The refined palette can be seen below:

![Refined Colour Palette for The Tavern](https://github.com/foster95/the_tavern/blob/main/documentation/brand/refined-colour-palette.png)

#### Typography
Using Our Own Thing's font matching extension, I settled on using Montserrat for the main body of the website, and Almendra for any headers. Montserrat is a standard font used across the industry, noted for its readability and simplicity. Almendra is a more decorative font which evokes the fantasy world, making it suited for The Tavern's aesthetics. Font Awesome was used for the social media icons in the footer and the general icons across the full website.  

![Google Fonts chosen for The Tavern](https://github.com/foster95/the_tavern/blob/main/documentation/brand/google-fonts.png)

#### The Tavern's Logo & Wordmark
### Wordmark
![Wordmark for The Tavern](https://github.com/foster95/the_tavern/blob/main/documentation/brand/wordmark-3.png)

### Logo
![Logo for The Tavern](https://github.com/foster95/the_tavern/blob/main/documentation/brand/outline-logo.webp)

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
* Users are able to receive a confirmation email once they have completed a product purchase  §a
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
* As a staff member (Admin role), I want to be able to delete product reviews, so that I can ensure that inappropriate reviews do not end up on the website
* As a staff member (Admin role), I want to be able to add, amend and delete products from the website 

#### User Account and Authentication
* As a user, I can sign up to become a registered user, so that I can track have a profile that tracks previous orders and automatically populate fields with my details at checkout
* As a user, I will receive a confirmation email when I have created an account, so that I can securely validate my account
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
* As a user of the website, I can receive an email confirming my order once my order has been successfully submitted

#### Brand Experience
* As a user, I want to be able to sign up to The Tavern's newsletter, so I can learn about their community
* As a user, I want to be able to see information about the company, so I can know who I'm buying from
* As a user, I want to be able to contact the team behind The Tavern, so I can know that I can message directly with questions, queries or suggestions
* As a staff member (Admin role) I want to be able to update the information on the company, so that I can keep this up to date as the company grows and expands

### MoSCoW Prioritisation
Using the MoSCoW priotisation method, I then further broke down my user stories into four separate categories. These categories are:
 
* Must Have - this should take up no more than 60% of the entire project. 
* Should Have
* Could Have
* Won't Have

Using GitHub's issue board, I grouped each user story by its category and then transferred these to the GitHub Projects kanban board which I used to track website progression over the remaining project

#### MoSCoW summary
| Priority | Count | Percentage
--- | --- | --- 
Must Have | 12 | 48%
Should Have | 10 | 40%
Could Have | 3 | 12%
Won't Have | 0 | 0%
Total | 25 | 100%

#### Must Have
* As a user of the website, I want to be able to browse products so that I can find items to purchase
* As a user of the website, I want to be able to view product details for each individual product, so that I can understand if the product is suited for my needs
* As a staff member (Admin role), I want to be able to add, amend and delete products from the website
* As a user, I can sign up to become a registered user, so that I can track have a profile that tracks previous orders and automatically populate fields with my details at checkout
* As a user, I will receive a confirmation email when I have created an account, so that I can securely validate my account
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
* As a user of the website, I can receive an email confirming my order once my order has been successfully submitted
* As a user, I want to be able to contact the team behind The Tavern, so I can know that I can message directly with questions, queries or suggestions

#### Could Have
* As a registered user, I am able to give myself a profile picture, so that I can have a photo on my profile
* As a user, I want to be able to see information about the company, so I can know who I'm buying from
* As a staff member (Admin role) I want to be able to update the information on the company, so that I can keep this up to date as the company grows and expands

### GitHub Issues
From the beginning of development, I used GitHub Issues as means to manage and create epics with user stories inside them, as well as build out the acceptance criteria for each user story.

### GitHub Boards
In the later stages of development I used GitHub Projects kanban board as a tracker. epics with user stories inside them, were placed in the To-do section and were steadily moved over as they were completed.

## Databse Design
### Data Models
Prior to building The Tavern, I created an ERD which helped me visualise all of the relationships between the different datasets and databases in the site. I used Miro to create this:
![Databse ERD](https://github.com/foster95/the_tavern/blob/main/documentation/database/erd.png)

## Website Features
### Header
The header extends the base.html template, and is a simple, minimalistic design which is visually appealing for users. On mobile the header is much simpler, displaying only the most crucial features of the website to allow users easy UX - these features are: a drop down burger icon which allows users to navigate to the following: all products, dice, other accessories, about us, FAQ and contact us. There is also a search button, allowing users to search the site, a my account button, and a basket button. On tablets and up, the header is much more elaborate, featuring a small version of the companies logo on the left hand side, a central search bar and the account and basket features on the right hand side of the screen. Running just below this in a separate bar is the product catalogue, and separated from this the FAQ and the contact us button can be found in the header. This allows users to easily navigate to the product directory, but requires them to search a little further for the other pages, which is the ultimate goal of an eCommerce site. 

### Newsletter Sign Up
The newsletter sign up extends from base.html and acts as part of an elongated footer. The newsletter is connected to Mailchimp, and on the user providing their email this is tracked in Mailchimp's dashboard. On providing the email, the user is shown a success message confirming that their information has been collected. 

### Footer
The footer also extends from base.html and is very simple, made up of a few links for users to navigate around the site, and to find the social media links for the company. All of the social media links apply the "rel=noopener" rule, and open to a new page away from the site. The footer is responsive to various screen sizes, stacking on mobiles, and stretching out from tablet onwards. 

### Scrolling Bar - Home Page
The scrolling bar is a fun little feature that allows users to see the free delivery threshold by scrolling across the screen. The scroll is slow so as not to be distracting, and can be stopped by hovering the mouse over the scroll bar. 

### Product of the Month - Home Page
The Product of the Month section of the homepage is linked to a template literal which comes from a model that was specifically built for this function. This model allows superadmin staff users to access the Django admin platform and highlight a specific product that they want to show on the website. 

        MONTH_CHOICES = [(i, calendar.month_name[i]) for i in range(1, 13)]

        class ProductOfTheMonth(models.Model):
            year = models.PositiveIntegerField()
            month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
            product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

        class Meta:
            unique_together = ("year", "month")
            ordering = ["-year", "-month"]
            verbose_name = "Product of the Month"
            verbose_name_plural = "Product of the Month"

        def __str__(self):
            try:
                month_int = int(self.month)
                month_label = calendar.month_name[month_int]
            except (TypeError, ValueError, IndexError):
                month_label = str(self.month)
            return f"Featured Product for {month_label} {self.year}: {self.product}"


### Reasons to Buy - Home Page
The reasons to buy carousel is a simple carousel made up of text which slides across every 7 seconds to the next item. The carousel is set to loop infinitely but is subtle enough that it should not cause any visual issues. Users can also toggle through to the next item using the arrows on either side of the page. 

### Testimonials - Home Page
The testimonials section is made up of another simple model, allowing staff to update the testimonials shown on the website. The testimonial is made up of a quote, a name, and a tag line (often the typical character a player goes by). They are able to update any testimonial, as well as add, delete and change the order of the testimonials. On a mobile screen, the testimonials automatically stack. 

        class Testimonial(models.Model):
            quote = models.TextField()
            name = models.CharField(max_length=80)
            tagline = models.CharField(max_length=120, blank=True) 
            sort_order = models.PositiveSmallIntegerField(default=0)

            created_at = models.DateTimeField(auto_now_add=True)

            class Meta:
                ordering = ["sort_order", "-created_at"]

            def __str__(self):
                return f"{self.name} — {self.quote[:40]}..."

### Product Catalog 
The product catalog is a visual map for users of the website to navigate to the product details of each individual product they want to find out more information about. Every item is associated to an image, a product name, a price (which either reads as flat price or a from price) and a tag by which users can filter (ie metallic dice, dice bag, dice tower). If a product does not have an image, a file has been loaded up in the media folder which kicks in as a default. Products can be ordered by the following: alphabetical order, price and category. There are two models associated with the product page, the Category model and the Product model. Within the model, there is a further function which automatically generates a sku for employees, and a function which generates a slug for the product which appears in the admin panel. 

        class Category(models.Model):
            """ Model for product categories """

            class Meta:
                verbose_name_plural = 'Categories'
                    name = models.CharField(max_length=254)
                    slug = models.SlugField(max_length=254, unique=True)
                    friendly_name = models.CharField(max_length=100, null=True, blank=True)

                def __str__(self):
                    return self.friendly_name or self.name
    
                def get_friendly_name(self):
                    return self.friendly_name

                def generate_sku(product):
                    category_code = product.category.slug[:3].upper() if product.category else "GEN"
                    material = (product.product_material or "STD")[:8].replace(" ", "").upper()
                    name_part = slugify(product.name).split("-")[-1][:6].upper()
                    unique = uuid.uuid4().hex[:4].upper()
                    return f"{category_code}-{material}-{name_part}-{unique}"
        

        class Product(models.Model):
            """ Model for products """

            class Meta:
                ordering = ['name']
            category = models.ForeignKey(
                'Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='products'
            )
            sku = models.CharField(max_length=50, null=True, blank=True, unique=True)
            name = models.CharField(max_length=254)
            slug = models.SlugField(max_length=254, unique=True, null=True, blank=True)
            description = models.TextField()
            product_material = models.CharField(max_length=254, null=True, blank=True)
            product_dimensions = models.CharField(max_length=254, null=True, blank=True)
            price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
            dice_set_price= models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
            image_url = models.URLField(max_length=1024, null=True, blank=True)
            image = models.ImageField(null= True, blank=True)

            def save(self, *args, **kwargs):
                if not self.slug:
                    self.slug = slugify(self.name)
            
                if not self.sku:
                    self.sku = generate_sku(self)
                
                super().save(*args, **kwargs)

            def __str__(self):
                return self.name

The product catalog is designed mobile first, and products stack into individual rows on a mobile, rows of two on a tablet and rows of four on desktop and above. There is a small arrow that floats on the right hand side of the items which takes users from the bottom of the page to the top using a small chunk of javascript. This code was inspired by the Boutique Ado walkthrough and adjusted for the project needs. 

### Product Details Page
Upon clicking any of the items on the product catalog, the user is taken to the individual product description page. Products are searched for using their slug, rather than their indiviudal ID number, providing better UX for users as they can understand the product they are searching for much easier than if they were required to know the product number. The product details page includes the following - the product tag, a product image, a product title, a product description, a product price, a product quantity toggler and a dimensions and materials drop down accordion. When accessed via mobile, the columns automatically stack on top of each other but on tablet and larger screens, the columns split into two showing the product image on the left hand side and the product details on the right. 

As dice can be sold either individually or as part of a seven piece set, dice have an additional option where users can choose whether or not they are buying the individual price, or the full set, which affects the price shown on the site. Dice products will automatically default to the single D20 price when the user loads onto the website. To determine whether or not the product is considered to be a flat price or part of the single vs set cost, the below model was created: 

        class Bundle(models.Model):
            """ Model for product bundles - ie is customer buying one d20 or a full set? """
            category = models.ForeignKey(
                Category,
                on_delete=models.CASCADE,
                related_name='bundle_prices'
            )
            name = models.CharField(max_length=100)
            quantity = models.PositiveIntegerField()
            price = models.DecimalField(max_digits=8, decimal_places=2)

            class Meta:
                unique_together = ('category', 'name')

            def __str__(self):
                return f"{self.category.name} - {self.name}"

A small portion of javascript was written to help the user in clicking between the single dice price and the full set price. 

        document.addEventListener("DOMContentLoaded", () => {
            const singleBtn = document.getElementById("single-btn");
            const setBtn = document.getElementById("set-btn");
            const priceSpan = document.getElementById("product-price");
            const diceOption = document.getElementById("dice-option");

            if (!singleBtn || !setBtn || !priceSpan || !diceOption) return;

            diceOption.value = "single";
            singleBtn.classList.add("active");
            setBtn.classList.remove("active");

            singleBtn.addEventListener("click", () => {
                diceOption.value = "single";
                priceSpan.textContent = singleBtn.dataset.price;

                singleBtn.classList.add("active");
                setBtn.classList.remove("active");
            });

            setBtn.addEventListener("click", () => {
                diceOption.value = "set";
                priceSpan.textContent = setBtn.dataset.price;

                setBtn.classList.add("active");
                singleBtn.classList.remove("active");
            });
        });

Users of the website can also input the quantity of the item they would like to add to their shopping bag. To avoid a user being able to input 0, a guard has been introduced through javascript, which does not allow the number 0 to be inputted and automatically defaults to 1 if they user does try and manually type to override:

        document.addEventListener("DOMContentLoaded", () => {
            const MIN_QTY = 1;
            const MAX_QTY = 99;

            document.querySelectorAll(".quantity-wrapper").forEach((wrapper) => {
                const minusBtn = wrapper.querySelector(".qty-btn.minus");
                const plusBtn = wrapper.querySelector(".qty-btn.plus");
                const input = wrapper.querySelector(".qty-input");

                if (!minusBtn || !plusBtn || !input) return;

                const updateButtons = () => {
                    minusBtn.disabled = parseInt(input.value) <= MIN_QTY;
                };

                if (!input.value || parseInt(input.value) < MIN_QTY) {
                    input.value = MIN_QTY;
                }
                updateButtons();

                minusBtn.addEventListener("click", () => {
                    let value = parseInt(input.value);

                if (value > MIN_QTY) {
                    input.value = value - 1;
                }

                updateButtons();
                });

                plusBtn.addEventListener("click", () => {
                    let value = parseInt(input.value);

                if (value < MAX_QTY) {
                    input.value = value + 1;
                }

                updateButtons();
                });

                input.addEventListener("input", () => {
                    let value = parseInt(input.value);

                if (isNaN(value) || value < MIN_QTY) {
                    input.value = MIN_QTY;
                }

                if (value > MAX_QTY) {
                    input.value = MAX_QTY;
                }

                updateButtons();
                });
            });
        });

On putting an item in the shopping bag, the website utilises Bootstraps built in toast system to indicate to the user that the item has been added to their bag. The toast has a X for users to close, but will also automatically fade after 5 seconds. Within the toast, the user is able to see the item that has been placed into the bag, the quantity of the item and the cost as well as see if they have put enough things in their shopping bag to get free delivery. Finally, the user is shown a button which takes them to the shopping bag page. 

### Shopping Bag
The shopping bag, or the Bag of Holding as it is called on the website in line with the D&D theme, is the next step in the purchasing process for a user, and is designed to give the user an immediate detailed overview of the products they are in the process of purchasing. The page is designed to be as simple as ossible, with a table which includes the product image, the item that is being purchased, the quantity and the subtotal. Underneath this, the user can see the bag total, delivery costs and the grand total. If the user has not reached the threshold for free delivery, they are informed how much more they need to spend to reach the free checkout threshold. Within the table, users are able to amend their product quantity, increasing or reducing it (no lower than 1) or removing the entire item from the bag. To wire up the quantity and remove buttons and make them functional, a small amount of JS was written which was inspired by the Boutique Ado code: 


        /* Bag quantity controls + prevent Update if quantity hasn't changed */

            document.addEventListener("DOMContentLoaded", () => {
            const MIN_QTY = 1;
            const MAX_QTY = 99;

            /* Quantity + / - controls */
            document.querySelectorAll(".quantity-wrapper").forEach((wrapper) => {
                const minusBtn = wrapper.querySelector(".qty-btn.minus");
                const plusBtn = wrapper.querySelector(".qty-btn.plus");
                const input = wrapper.querySelector(".qty-input");

                if (!minusBtn || !plusBtn || !input) return;

                const clamp = (val) => Math.min(MAX_QTY, Math.max(MIN_QTY, val));

                const sync = () => {
                const val = parseInt(input.value, 10);
                input.value = clamp(isNaN(val) ? MIN_QTY : val);
                minusBtn.disabled = parseInt(input.value, 10) <= MIN_QTY;
                };

                sync();

                minusBtn.addEventListener("click", () => {
                input.value = clamp(parseInt(input.value, 10) - 1);
                sync();
                });

                plusBtn.addEventListener("click", () => {
                input.value = clamp(parseInt(input.value, 10) + 1);
                sync();
                });

                input.addEventListener("input", sync);
            });

            /* Block Update if unchanged */
            let warningShown = false;

            document.querySelectorAll("form").forEach((form) => {
                const input = form.querySelector(".qty-input");
                const updateBtn = form.querySelector(".bag-update-button, .update-button");

                // Only target update forms
                if (!input || !updateBtn) return;

                // Reset warning if user changes quantity
                input.addEventListener("input", () => {
                warningShown = false;
                });

                form.addEventListener("submit", (e) => {
                const original = parseInt(input.dataset.original, 10);
                const current = parseInt(input.value, 10);

                if (isNaN(original)) return;

                if (original === current) {
                    e.preventDefault();

                    if (!warningShown) {
                    showBagMessage("Quantity hasn’t changed.");
                    warningShown = true;
                    }
                }
                });
            });
            });

            /* Block Update if unchanged */
            function showBagMessage(text) {
            const toastEl = document.getElementById("js-toast-warning");
            const textEl = document.getElementById("js-toast-warning-text");

            if (!toastEl || !textEl) return;

            textEl.textContent = text;

            // unhide the toast only when needed
            toastEl.classList.remove("d-none");

            const toast = bootstrap.Toast.getOrCreateInstance(toastEl);
            toast.show();
            }

            document.addEventListener("DOMContentLoaded", () => {
            const toastEl = document.getElementById("js-toast-warning");
            if (!toastEl) return;

            toastEl.addEventListener("hidden.bs.toast", () => {
                toastEl.classList.add("d-none");
            });
            });

The code has two versions - a mobile version and a desktop version, which changes dependent on how the user is accessing the bag. On mobile the table cannot be seen and all of the items stack into readable columns. The buttons are still accessible, allowing users to increase or decrease quantity, and the bin button can be used to remove the item from the bag. Provided the user is happy with everything, they are able to proceed to the next stage of the secure checkout via a button. If they would like to go back and add more items to their shopping bag, there is another button which returns them to the product catalog. 

### Checkout

## Developmental Bugs
Throughout development I came across numerous issues, bugs and difficulties with the website. At the time of submission, I am confident there are no bugs remaining, however I cannot guarantee this 100% as I cannot account for all user behaviour that would try to break the website and its integrity. The vast majority of the bugs that I came across were to do with minor CSS and responsivity issues, however the major bug that I struggled with has been documented below:

### AWS S3 Media Storage
As part of preparing The Tavern for production, I migrated media storage from local filesystem storage to AWS S3. The goal was to ensure scalable, persistent media storage suitable for deployment on Heroku. Although the initial configuration appeared successful, the migration introduced a series of subtle but significant issues that required deep debugging across storage configuration, database records, and template rendering.

After implementing S3, I observed inconsistent behaviour in production. Some product images rendered correctly, while others failed to display. Newly uploaded images sometimes appeared, but older ones did not. Additionally, the default “missing image” fallback — which worked locally — did not display at all in production. At first glance, the issue seemed unpredictable, but further investigation revealed that the inconsistencies were rooted in how Django stores file paths in the database and how those paths map to S3 object keys. I discovered that some products had been created before the migration, and their stored file paths did not align with the S3 folder structure. As a result, Django generated URLs that pointed to non-existent objects in the bucket. This explained why some images worked and others returned 404 errors — the database was referencing files that did not exist in the expected S3 location.

The issue with the default fallback image was slightly different. The file existed locally in the project’s media directory, but it had never been uploaded to S3. To fix this I moved the missing image from the media products folder to the static images folder. 

To resolve this issue, I conducted systematic checks between Django admin, the folders in VSCode and S3 in AWS. In the end, I decided to remove all of the original file photos from the media file, and reuploading them through the deployed website to ensure that the files were saved into AWS rather than locally. The same files were then duplicated and placed into folders in local development to avoid any confusion for myself. This also supported my performance issues, as Google Lighthouse was highlighting that the photos being hosted were too large and were causing loading issues. As such all of the files that exist within the website have been reformatted to WebPs that were further compressed to reduce the file size. At the time of submission, this issue has been fully fixed.

### Stripe Webhooks
Similarly to the AWS issue, the issue with webhooks wasn't uncovered until the the website was put into production and I was conducting general testing with the full checkout path from browsing to purchase. Post purchase, I discovered that emails were not being sent automatically due to the set up of the Webhooks. To discover this I did a combination of close monitoring of the webooks event section, and using Heroku's live logging system which allowed me to see in realtime that the webhooks weren't triggering for email sending. 

Part of this issue was resolved quickly after I realised that there were a number of issues and inconsistencies with my env.py credentials and in the settings.py folder for email settings, which I fixed. On fixing this, the emails did begin to send, however they began to send in duplicate, particularly when the website was running slowly. To fix this, I added the following to the order model:

            confirmation_email_sent = models.BooleanField(default=False)

After running the standard migrations required for the model, I updated the webhook logic which searched for the confirmation email sent boolean and decides whether or not to send an email. Further, this webhook acted so if it sent the email, it was automatically toggle that boolean from false to true, which wouldn't allow for duplicate emails. 

## Testing
Multiple testing methods were carried out to ensure the quality, functionality, and responsiveness of The Tavern. These included automated validation tools, device and browser testing, Lighthouse analysis, accessibility checks, and user-story-based manual testing. All core functionality works as expected and, at the time of submission, all known bugs have been resolved.

### Summary of Testing
Testing Method | Tools Used | Purpose | Result 
--- | --- | --- | ---
Performance | Google Lighthouse | Measure performance & best practices | Good overall 
HTML Validation | Nu HTML Checker | Check HTML structure | Passed – 0 errors 
CSS Validation | W3C CSS Validator | Validate custom CSS | Passed – 0 errors 
JavaScript Validation | JSHint | Validate ES6 syntax | Passed 
Python Validation | CI PEP8 Linter | Check PEP8 compliance | Passed across apps 
Accessibility | WAVE | WCAG & ARIA validation | Minor contrast issue 
Browser Testing | Chrome, Safari, Firefox, Edge | Cross-browser consistency | Passed 
Device Testing | iPhone, Android, Tablet, Desktop | Cross-device consistency | Passed
Manual Testing | Developer testing | To test that all website features were working manually | Passed
User Story Testing | Manual testing table | Verify all features against stories | Good overall 

### Lighthouse Testing
As part of general testing, I conducted a series of lighthouse tests across both mobile and desktop formatting. As a rule of thumb, all of the tests for mobile came back weaker than desktop, however from doing research this seems to be an issue connected to the fact that the website is hosted through Heroku on eco dynos and therefore is not primed to hit high grades. The weakest page was the products directory page, which was to be expected as the page is very image and link heavy, due to being an eCommerce website. To try and reduce image size, all images were reformatted from JPEGs to WebPs and were then further compressed. Lazy loading was also used on almost all of the photos, helping reduce the photo weight. 

| Page | Format | Lighthouse Grades
--- | --- | --- 
Home | Desktop | ![Desktop - Home Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-base.png)
Home | Mobile | ![Mobile - Home Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-base.png)
Products | Desktop | ![Desktop - Products Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-products.png)
Products | Mobile | ![Mobile - Products Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-products.png)
Product Details | Desktop | ![Desktop - Product Details Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-product-details.png)
Product Details | Mobile | ![Mobile - Product Details Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-product-details.png)
Add Product | Desktop | ![Desktop - Add Product Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-add-product.png)
Add Product | Mobile | ![Mobile - Add Product Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-add-product.png)
Amend Product | Desktop | ![Desktop - Amend Product Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-amend-product.png)
Amend Product | Mobile | ![Mobile - Amend Product Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-amend-product.png)
Bag | Desktop | ![Desktop - Bag Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-bag.png) 
Bag | Mobile | ![Mobile - Bag Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-bag.png)
Checkout | Desktop | ![Desktop - Checkout Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-checkout.png)
Checkout | Mobile | ![Mobile - Checkout Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-checkout.png)
Order Confirmation | Desktop | ![Desktop - Order Confirmation Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-order-confirmation.png)
Order Confirmation | Mobile | ![Mobile - Order Confirmation Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-order-confirmation.png)
Profile | Desktop | ![Desktop - Profile Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-profile.png)
Profile | Mobile | ![Mobile - Profile Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-profile.png)
Contact | Desktop | ![Desktop - Contact Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-contact.png)
Contact | Mobile | ![Mobile - Contact Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-contact.png)
About | Desktop | ![Desktop - About Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-about.png)
About | Mobile | ![Mobile - About Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-about.png)
FAQ | Desktop | ![Desktop - FAQ Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-faq.png)
FAQ | Mobile | ![Mobile - FAQ Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-faq.png)
Privacy | Desktop | ![Desktop - Privacy Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-privacy.png)
Privacy | Mobile | ![Mobile - Privacy Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-privacy.png) 
Returns | Desktop | ![Desktop - Returns Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-returns.png)
Returns | Mobile | ![Mobile - Returns Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-returns.png)
Shipping | Desktop | ![Desktop - Shipping Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-shipping.png)
Shipping | Mobile | ![Mobile - Shipping Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-shipping.png)
Sign In | Desktop | ![Desktop - Sign In Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-sign-in.png)
Sign In | Mobile | ![Mobile - Sign In Lighthouse Grade](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-sign-in.png)
Sign In - Google | Desktop | ![Desktop - Sign In - Google](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-sign-in-google.png)
Sign In - Google | Mobile | ![Mobile - Sign In - Google](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-sign-in-google.png)
Sign In - Facebook | Desktop | ![Desktop - Sign In - Facebook](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-sign-in-facebook.png)
Sign In - Facebook | Mobile | ![Mobile - Sign In - Facebook](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-sign-in-facebook.png)
Sign Out | Desktop | ![Desktop - Sign Out](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-sign-out.png)
Sign Out | Mobile | ![Mobile - Sign Out](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-sign-out.png)
Sign Up | Desktop | ![Desktop - Sign Up](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/desktop-sign-up.png)
Sign Up | Mobile | ![Mobile - Sign Up](https://github.com/foster95/the_tavern/blob/main/documentation/lighthouse/mobile-sign-up.png)

### HTML Testing
| Page | Report | Notes
--- | --- |---
Home | ![HTML Validation - Home](https://github.com/foster95/the_tavern/blob/main/documentation/html/home.png) |
Products | ![HTML Validation - Products](https://github.com/foster95/the_tavern/blob/main/documentation/html/products.png) | 
Product Details | ![HTML Validation - Product Details](https://github.com/foster95/the_tavern/blob/main/documentation/html/product-details.png) |
Add Product | ![HTML Validation - Add Product](https://github.com/foster95/the_tavern/blob/main/documentation/html/product-add.png) | Minor info warning due to trailing slashes implemented by Django forms. Unfixed due to insignificance. 
Amend Product | ![HTML Validation - Amend Product](https://github.com/foster95/the_tavern/blob/main/documentation/html/product-amend.png) | Minor info warning due to trailing slashes implemented by Django forms. Unfixed due to insignificance. 
Bag | ![HTML Validation - Bag](https://github.com/foster95/the_tavern/blob/main/documentation/html/bag.png) |
Checkout | ![HTML Validation - Checkout](https://github.com/foster95/the_tavern/blob/main/documentation/html/checkout.png) |
Order Confirmation | ![HTML Validation - Order Confirmation](https://github.com/foster95/the_tavern/blob/main/documentation/html/checkout-confirmation.png) |
Profile | ![HTML Validation - Profile](https://github.com/foster95/the_tavern/blob/main/documentation/html/profile.png) | Minor info warning due to trailing slashes implemented by Django forms. Unfixed due to insignificance. 
Contact | ![HTML Validation - Contact](https://github.com/foster95/the_tavern/blob/main/documentation/html/contact.png) |
About | ![HTML Validation - About](https://github.com/foster95/the_tavern/blob/main/documentation/html/about.png) |
FAQ | ![HTML Validation - FAQ](https://github.com/foster95/the_tavern/blob/main/documentation/html/faq.png) |
Privacy | ![HTML Validation - Privacy](https://github.com/foster95/the_tavern/blob/main/documentation/html/privacy.png) |
Returns | ![HTML Validation - Returns](https://github.com/foster95/the_tavern/blob/main/documentation/html/returns.png)|
Shipping | ![HTML Validation - Shipping](https://github.com/foster95/the_tavern/blob/main/documentation/html/shipping.png) |
Sign In | ![HTML Validation - Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/html/login.png) |
Sign Out | ![HTML Validation - Sign Out](https://github.com/foster95/the_tavern/blob/main/documentation/html/logout.png) |
Sign Up | ![HTML Validation - Sign Up](https://github.com/foster95/the_tavern/blob/main/documentation/html/signup.png) |
Sign In - Google | ![HTML Validation - Sign In - Google](https://github.com/foster95/the_tavern/blob/main/documentation/html/google-login.png) |
Sign In - Facebook | ![HTML Validation - Sign In - Facebook](https://github.com/foster95/the_tavern/blob/main/documentation/html/facebook-login.png) |

### CSS Testing

### WAVE AimWeb Accessibility Testing


### PEP8 Testing
#### Home
| File | PEP8 Response
--- | ---
Admin | ![PEP8 Validation - Home/Admin](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/home-admin.png)
Apps | ![PEP8 Validation - Home/Apps](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/home-apps.png)
Models | ![PEP8 Validation - Home/Models](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/home-models.png)
URLs | ![PEP8 Validation - Home/URLS](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/home-urls.png)
Views | ![PEP8 Validation - Home/Views](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/home-views.png)

#### Products
| File | PEP8 Response
--- | ---
Admin | ![PEP8 Validation - Products/Admin](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/products-admin.png)
Apps | ![PEP8 Validation - Products/Apps](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/products-apps.png)
Forms | ![PEP8 Validation - Products/Forms](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/products-forms.png)
Models | ![PEP8 Validation - Products/Models](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/products-models.png)
URLs | ![PEP8 Validation - Products/URLS](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/products-urls.png)
Views | ![PEP8 Validation - Products/Views](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/products-views.png)

#### Bag
| File | PEP8 Response
--- | ---
Admin | ![PEP8 Validation - Bag/Admin](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/bag-admin.png)
Apps | ![PEP8 Validation - Bag/Apps](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/bag-apps.png)
Contexts | ![PEP8 Validation - Bag/Contexts](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/bag-contexts.png)
Models | ![PEP8 Validation - Bag/Models](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/bag-models.png)
URLs | ![PEP8 Validation - Bag/URLS](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/bag-urls.png)
Views | ![PEP8 Validation - Bag/Views](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/bag-views.png)

#### Checkout
| File | PEP8 Response
--- | ---
Admin | ![PEP8 Validation - Checkout/Admin](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-admin.png)
Apps | ![PEP8 Validation - Checkout/Apps](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-apps.png)
Forms | ![PEP8 Validations - Checkout/Forms]()
Models | ![PEP8 Validation - Checkout/Models](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-models.png)
Signals | ![PEP8 Validation - Checkout/Signals](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-signals.png)
URLs | ![PEP8 Validation - Checkout/URLS](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-urls.png)
Views | ![PEP8 Validation - Checkout/Views](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-views.png)
Webhook-Handler | ![PEP8 Validation - Checkout/Webhook-Handler](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-webhook-handler.png)
Webhooks | ![PEP8 Validation - Checkout/Webhooks](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/checkout-webhooks.png)

#### Profiles
| File | PEP8 Response
--- | ---
Admin | ![PEP8 Validation - Profiles/Admin](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/profiles-admin.png)
Apps | ![PEP8 Validation - Profiles/Apps](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/profiles-apps.png)
Forms | ![PEP8 Validation - Profiles/Forms](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/profiles-forms.png)
Models | ![PEP8 Validation - Profiles/Models](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/profiles-models.png)
URLs | ![PEP8 Validation - Profile/URLS](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/profiles-urls.png)
Views | ![PEP8 Validation - Profile/Views](https://github.com/foster95/the_tavern/blob/main/documentation/pep8/profiles-views.png)

### JShint Testing
| File | JShint
--- | ---
newsletter.js | ![JShint Validation - Newsletter](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/newsletter.png)
bag.js | ![JShint Validation - Bag](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/bag.png)
stripe_elements.js | ![JShint Validation - Stripe_Elements](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/stripe-elements.png)
product_details.js | ![JShint Validation - Product_Details](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/product-details.png)
product_form.js | ![JShint Validation - Product_Form](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/product-form.png)
product_review.js | ![JShint Validation - Product_Review](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/product-review.png)
products.js | ![JShint Validation - Products](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/products.png)
profile.js | ![JShint Validation - Profile](https://github.com/foster95/the_tavern/blob/main/documentation/jshint/profile.png)

### Device Testing
I used Blisk to conduct device testing across multiple devices

| Type of Device | Devices Tested | Page | Screenshot | Notes
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Home | ![Mobile - Home](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-home.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Navigation Dropdown | ![Mobile - Navigation Dropdown](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-navigation.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Search | ![Mobile - Search](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-search.png) 
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Products | ![Mobile - Products](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-products.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Product Details | ![Mobile - Product Details](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-product-details.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Bag | ![Mobile - Bag](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-bag.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Checkout | ![Mobile - Checkout](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-checkout.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Order Confirmation | ![Mobile - Order Confirmation](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-order-confirmation.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Profile | ![Mobile - Profile](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-profile.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Sign In - Standard | ![Mobile - Standard Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-sign-in.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Sign In - Google | ![Mobile - Google Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-google-login.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Sign In - Facebook | ![Mobile - Facebook Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-facebook-login.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Sign Up | ![Mobile - Sign Up](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-sign-up.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Sign Out | ![Mobile - Sign Out](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-sign-up.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | About ![Mobile - About](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-about.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | FAQ | ![Mobile - FAQ](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-faq.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Contact | ![Mobile - Contact](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-contact.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Returns | ![Mobile - Returns ](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-returns.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Shipping | ![Mobile - Shipping](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-shipping.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Privacy Policy | ![Mobile - Privacy](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-privacy-policy.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Add Product | ![Mobile - Add Product](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-admin-add-product.png)
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14 Pro, iPhone 13 Mini, iPhone 11 | Amend Product ![Mobile - Amend Product](https://github.com/foster95/the_tavern/blob/main/documentation/device/mobile-admin-amend-product.png)


Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Home | ![Desktop - Home](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-about.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Products | ![Desktop - Products](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-products.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Product Details | ![Desktop - Product Details](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-product-details.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Bag | ![Desktop - Bag](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-bag.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Checkout | ![Desktop - Checkout](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-checkout.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Order Confirmation | ![Desktop - Order Confirmation](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-order-confirmation.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Profile | ![Desktop - Profile](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-profile.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Sign In - Standard | ![Desktop - Standard Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-sign-in.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Sign In - Google | ![Desktop - Google Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-google-login.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Sign In - Facebook | ![Desktop - Facebook Sign In](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-facebook-login.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Sign Up | ![Desktop - Sign Up](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-sign-up.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Sign Out | ![Desktop - Sign Out](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-sign-out.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | About | ![Desktop - About](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-about.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | FAQ | ![Desktop - FAQ](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-faq.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Contact | ![Desktop - Contact](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-contact.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Returns | ![Desktop - Returns](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-returns.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Shipping | ![Desktop - Shipping](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-shipping.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Privacy Policy | ![Desktop - Privacy](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-privacy.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Add Product | ![Desktop - Add Product](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-add-product.png)
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina 4K | Amend Product ![Desktop - Amend Product](https://github.com/foster95/the_tavern/blob/main/documentation/device/desktop-amend-profile.png)

### Manual Testing
#### Base/General
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Header Bar | Header Bar is responsive to device | On tablets and desktops the header bar should show in full, stretching out across the full page with the logo on the left-handside, the search bar in the centre and the account icon and basket icon on the right hand side. On mobiles, this bar should not be seen at all, but the user sees the burger icon, the search icon, the account icon and the basket icon. On clicking the search icon, the search bar drops down and appears | On tablets and desktops the header bar shows in full, stretching out across the full page with the logo on the left-handside, the search bar in the centre and the account icon and basket icon on the right hand side. On mobiles, this bar cannot be seen at all, but the user sees the burger icon, the search icon, the account icon and the basket icon. On clicking the search icon, the search bar drops down and appears
Navigation Bar | Navigation Bar is responsive to device | On tablets and desktops the gold navigation bar should show, stretching across the full page. Within the navigation bar should be three columns - one for "All Products", one for "Dice" and one for "Other Accessories". On hovering over these, a further box should drop down from which the user can select what they would like. On mobiles, this bar should not show at all but a list of the items can be triggered by clicking the burger button. When the user clicks the burger button, they should also see the additional links to "Home", "Our Story", "FAQ", "Shipping", "Returns" and "Contact" | On tablets and desktops the gold navigation bar shows, stretching across the full page. Within the navigation bar are three columns - one for "All Products", one for "Dice" and one for "Other Accessories". On hovering over these, a further box drops down from which the user can select what they would like. On mobiles, this bar does not show at all but a list of the items can be triggered by clicking the burger button. When the user clicks the burger button, they can also see the additional links to "Home", "Our Story", "FAQ", "Shipping", "Returns" and "Contact" 
Scrolling Bar | Scrolling bar shows and scrolls across the page | The scrolling bar should be seen at the top of the page, underneath the gold navigation bar. The scroll should be relatively slow and should stop when the user clicks or hovers over the bar. The price of the free delivery should be taken from the Free Delivery threshold in settings.py | The scrolling bar is seen at the top of the page, underneath the gold navigation bar. The scroll is relatively slow and stops when the user clicks or hovers over the bar. The price of the free delivery is taken from the Free Delivery threshold in settings.py
Newsletter | Newsletter is functioning | The newsletter sign up function should be seen regardless of the device used. The user should be able to input their email and click subscribe. On clicking subscribe they should see the message "Welcome Adventurer! You are now subscribed to our newsletter!". The email should be recorded in the Mailchimp dashboard |  The newsletter sign up function can be seen regardless of the device used. The user is able to input their email and click subscribe. On clicking subscribe they  see the message "Welcome Adventurer! You are now subscribed to our newsletter!". The email is recorded in the Mailchimp dashboard
Footer | Footer is responsive | Footer should be responsive to the device. On mobiles the footer should stack into one column, and on desktops this should stretch out into three separate columns until it sits neatly. Social media icons should stretch out into one row when viewed on a desktop. | Footer is responsive to the device. On mobiles the footer stacks into one column, and on desktops this stretches out into three separate columns until it sits neatly. Social media icons stretch out into one row when viewed on a desktop.
Footer | Social Media links and other internal links | Social media links should open to a new tab. Internal links should just move the user to the correct page within the current tab | Social media links open to a new tab. Internal links move the user to the correct page within the current tab. 
Buttons | Buttons invert colour | Buttons should invert colour when hovered over to indicate to the user where they are hovering | Buttons invert colour when hovered over to indicate to the user where they are hovering
Toasts | Toasts trigger | Toasts should trigger when required across the site, including but not limited to - any state change to the bag, any confirmation order, any state change to the users account, login and log out | Toasts trigger when required across the site, including but not limited to - any state change to the bag, any confirmation order, any state change to the users account, login and log out 

#### Home 
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Home Page | User opens to The Tavern | User opens The Tavern and is automatically taken to the homepage | User opens The Tavern and is automatically taken to the homepage
Home Page | Logo (tablets and desktops only) | User clicks on the logo and the page reloads to the homepage | User clicks on the logo and the page reloads to the homepage
Hero Image | Hero image shows | Hero image should be seen at the top of the page underneath the scroll bar. The hero image should be responsive to the device | Hero image should be seen at the top of the page underneath the scroll bar. The hero image should be responsive to the device | Hero image is seen at the top of the page underneath the scroll bar. The hero image is responsive to the device
Product of the Month/Explore our Wares | Section is responsive | On mobiles, Product of the Month should stack on top of the Explore our Wares section. On tablets and up, this should stretch out into one long row, with the Product of the Month section on the left, and the Explore our Wares section on the right. The buttons for Explore our Wares should remain stacked regardless of whether accessed on a mobile, tablet or desktop | On mobiles, Product of the Month stacks on top of the Explore our Wares section. On tablets and up, this stretches out into one long row, with the Product of the Month section on the left, and the Explore our Wares section on the right. The buttons for Explore our Wares remain stacked regardless of whether accessed on a mobile, tablet or desktop
Product of the Month | Product of the Month can be seen and is showing accurate information | Product of the Month image should show the relevant item as decided by the Django admin panel. Users should also be able to see the name of the product, and the cost. The name of the product should be a clickable link that takes the user to the product details page for that item. The Product of the Month should be set by the admin panel, which can be pre-planned by the superadmin who is logged in. | Product of the Month image shows the relevant item as decided by the Django admin panel. Users are able to see the name of the product, and the cost. The name of the product is a clickable link that takes the user to the product details page for that item. The Product of the Month is be set by the admin panel, which can be pre-planned by the superadmin who is logged in.
Explore our Wares Buttons | Buttons are working | The relevant buttons should take the user to the associated part of the site. On hovering over the button the colour should invert to indicate to the user where they are clicking | The relevant buttons take the user to the associated part of the site. On hovering over the button the colour inverts to indicate to the user where they are clicking
Reasons to Purchase Carousel | Carousel shows carousel of text which slides automatically | Carousel should render as a full green block that stretches across the entire page, regardless of device. The carousel should change on a slide every seven sessions, but there should also be arrows on either side for users to click through if they desire. The reason should be broken up into a small header, and slightly more explanation underneath. Underneath the entire carousel, users should see "Trusted by tables across the UK." | Carousel renders as a full green block that stretches across the entire page, regardless of device. The carousel changes on a slide every seven sessions, and there are also arrows on either side for users to click through if they desire. The reason is be broken up into a small header, and slightly more explanation underneath. Underneath the entire carousel, users can see "Trusted by tables across the UK."
Testimonials | Testimonials should be responsive | Testimonials should stack on mobile and stretch into a full row of three separate columns on desktops | Testimonials stack on mobile and stretch into a full row on three separate columns on desktop
Testimonials | Testimonials should render and should show accurate testimonials as set up in the Django Admin | Testimonials should render as the following - a small paragraph with the testimonial and underneath that, the name of the person providing a testimonial, the class/race they typically play, and their location as a subheader. The testimonial that shows should match the information that has been set in the Django Admin, including the order set on the admin | Testimonials render as the following - a small paragraph with the testimonial and underneath that, the name of the person providing a testimonial, the class/race they typically play, and their location as a subheader. The testimonial that shows matches the information that has been set in the Django Admin, including the order set on the admin

#### Products
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Products Page | Products page renders showing the product catalog and is responsive | The product page should render when loaded and display the catalog. It should be responsive to the device used, stacking into a single column on mobiles, and stretching out into four columns per row on desktops. | The product page renders when loaded and displays the catalog. It is responsive to the device used, stacking into a single column on mobiles, and stretching out into four columns per row on desktops.
Products Page | Filter | The sort by filters should work as the following: Price (low to high), Price (high to low), Name (A-Z), Name (Z-A), Category (A-Z), Category (Z-A). They should all be reset by clicking back onto the "Sort by" option which reloads all of the categories by A-Z | The sort by filters works as the following: Price (low to high), Price (high to low), Name (A-Z), Name (Z-A), Category (A-Z), Category (Z-A). They can all be reset by clicking back onto the "Sort by" option which reloads all of the categories by A-Z 
Product Page | Product image renders | Product image should render regardless of device | Product image renders regardless of device
Product Page | Product name, price and category renders and is correct according to Django Admin | Product name, price and category should render underneath the product image, and should match the information in the Django Admin | Product name, price and category renders underneath the product image, and matches the information in the Django Admin
Product Page | Product Price | Product price should show as the flat cost for dice towers, dice bags and dice boxes. Dice should show as a "From" price, which should be the lowest possible price of the dice set as declared in the Django Admin | Product price is shown as the flat cost for dice towers, dice bags and dice boxes. Dice show as a "From" price, which is the lowest possible price of the dice set as declared in the Django Admin 
Product Page | Edit and Delete buttons show only when the Superuser is logged in | The Edit and Delete buttons which launch the product amendment pages or delete the product from the catalog should only be visible for Superadmins. Normal users should not see these buttons at all | The Edit and Delete buttons which launch the product amendment pages or delete the product from the catalog are only be visible for Superadmins. Normal users do not see these buttons at all
Products Page | Back to Top button | The Back to Top button should appear once the user begins to scroll on the lower right hand side of the screen regardless of the device. On clicking this button, the site should scroll back to the top of the page | The Back to Top button appears once the user begins to scroll on the lower right hand side of the screen regardless of the device. On clicking this button, the site scrolls back to the top of the page

#### Product Details
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Product Details | Product Details page renders and is responsive to device | Product page should render with the following: a product image, the product title, the product description, the product materials and dimensions accordion, the product quantity toggle, the add to bag button, and the product image and customer reviews if they have been provided by users. On mobiles this should all stack into one long column, on desktops this should stretch out where the product and product details should be two columns on the same row, with the image on the left-handside and the product details on the right. The product reviews should show under this in a completely different row | Product page renders with the following: a product image, the product title, the product description, the product materials and dimensions accordion, the product quantity toggle, the add to bag button, and the product image and customer reviews if they have been provided by users. On mobiles this stacks into one long column, on desktops this stretches out and the product and product details are in two columns on the same row, with the image on the left-handside and the product details on the right. The product reviews show under this in a completely different row.
Product Details | Choose option renders on dice | If a user loads the product details for a dice set, they should be able to see the option of the single D20 or the full set. The page should automatically load to the single D20 cost. The price shown on the page should reflect the costs set in the Django Admin for the single D20 vs the full set when the user flicks between the buttons and should update in realtime | If a user loads the product details for a dice set, they are able to see the option of the single D20 or the full set. The page automatically loads to the single D20 cost. The price shown on the page reflects the costs set in the Django Admin for the single D20 vs the full set, and when the user flicks between the buttons updates in realtime
Product Details | Product quantity increase and decrease button works and updates quantity in real time | The product quantity increase and decrease buttons should update when being clicked by a user. The quantity number should update as this goes up and down in real time and should the user add the item to their bag, the quantity should match the quantity in the bag. | The product quantity increase and decrease buttons update when being clicked by a user. The quantity number updates as this goes up and down in real time and should the user add the item to their bag, the quantity matches the quantity in the bag.
Product Details | Product quantity cannot be reduced lower than 1 | The product quantity should not be able to be reduced lower than 1, even if the user tries to override this by manually typing 0 | Product quantity cannot be reduced lower than 1, even when the user tries to override this by manually typing 0
Product Details | Add to bag button | Add to bag button should add the items to a session bag, which is connected to the quantity shown in the product quantity toggle. On clicking add to bag, a toast should be launched which says the item has been added to the bag | Add to bag button adds the items to a session bag, which is connected to the quantity shown in the product quantity toggle. On clicking add to bag, a toast launches which says the item has been added to the bag
Product Details | Product Material and Dimension Accordion | The "Product Material" and "Product Dimensions" accordion should activate when a user clicks the accordion bar. The accordions should be able to be opened independently and closed independently rather than opening and closing together | The "Product Material" and "Product Dimensions" accordion activates when a user clicks the accordion bar. The accordions can be opened independently and closed independently rather than opening and closing together 
Product Page | Edit and Delete buttons show only when the Superuser is logged in | The Edit and Delete buttons which launch the product amendment pages or delete the product from the catalog should only be visible for Superadmins. Normal users should not see these buttons at all | The Edit and Delete buttons which launch the product amendment pages or delete the product from the catalog are only be visible for Superadmins. Normal users do not see these buttons at all
Product Details | Reviews | Reviews can only be provided by people who are logged in | Users should be logged in to provide a review. If the user is logged out, they should be sent to the login page. | Users must be logged in to provide a review. If the user is logged out, they are sent to the login page.
Product Details | Reviews | Reviews do not automatically get submitted for view | Reviews provided and submitted should not immediately be published, instead the review should go to "pending" and should only be approved by a Superuser. Until the review has been approved, the user that provided the review should see the review as "pending" and it should not be published to the website | Reviews provided and submitted are not immediately published, instead the review goes to "pending" and can only be approved by a Superuser. Until the review has been approved, the user that provided the review should see the review as "pending" and it is not published to the website
Product Details | Reviews | Edit reviews go back to pending | If a review has been approved and the user wishes to make a change, any change should force the comment back to a pending state which should be reapproved by the Superadmin again. Whilst the review is "pending" the review should show as "pending" | If a review has been approved and the user wishes to make a change, any change forces the comment back to a pending state which has to be reapproved by the Superadmin again. Whilst the review is "pending" the review shows as "pending" 
Product Details | Reviews | Rating gets aggregated with multiple reviews | If a review has multiple reviews, the rating shown at the top should be an aggregate of the stars given | If a review has multiple reviews, the rating shown at the top is an aggregate of the stars given
Product Details | Profile Picture | Profile picture should be the correct profile picture for the account user, and if the user has not uploaded a profile picture, should be the default picture instead | Profile picture is the correct profile picture for the account user, and if the user has not uploaded a profile picture, this is the default picture instead

#### Bag
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Bag | Bag page renders and is responsive to device | The bag page should render according to how it is being accessed. On mobiles, the product bag should render into a single column, with a horizontal divider between each item to segregate. On tablets and above it should render into a table with columns and rows underneath. On mobiles the bag should render as the following: an image, the product name, the SKU, the price, the product quantity toggler, a bin icon, an update button and a subtotal. Underneath the horizontal divider, there should be a bag total, a delivery cost and a grand total. Under this, two buttons should show which allow the user to either return to the product page or proceed to the checkout. On tablets and above the bag should render as a table, with the following: the product image, the product title and SKU, the price, the quantity, an update button, a bin icon and a subtotal. Underneath the table, there should be a bag total, a delivery cost and a grand total. Under this, two buttons should show which allow the user to either return to the product page or proceed to the checkout. | The bag page renders according to how it is being accessed. On mobiles, the product bag renders into a single column, with a horizontal divider between each item to segregate. On tablets and above it renders into a table with columns and rows underneath. On mobiles the bag renders as the following: an image, the product name, the SKU, the price, the product quantity toggler, a bin icon, an update button and a subtotal. Underneath the horizontal divider, there is the bag total, a delivery cost and a grand total. Under this, two buttons show which allow the user to either return to the product page or proceed to the checkout. On tablets and above the bag renders as a table, with the following: the product image, the product title and SKU, the price, the quantity, an update button, a bin icon and a subtotal. Underneath the table, there is a bag total, a delivery cost and a grand total. Under this, two buttons  show which allow the user to either return to the product page or proceed to the checkout.
Bag | Product quantity increase and decrease button works and updates quantity in real time | The product quantity increase and decrease buttons should update when being clicked by a user. The quantity number should update as this goes up and down in real time and should the user add the item to their bag, the quantity should match the quantity in the bag | The product quantity increase and decrease buttons updates when being clicked by a user. The quantity number updates as this goes up and down in real time and should the user add the item to their bag, the quantity matches the quantity in the bag
Bag | Product quantity cannot be reduced lower than 1 | The product quantity should not be able to be reduced lower than 1, even if the user tries to override this by manually typing 0 | Product quantity cannot be reduced lower than 1, even when the user tries to override this by manually typing 0
Bag | Bag update button works | On clicking the update button, the following should update: the quantity, the subtotal, bag total, grand total and any delivery costs associated. A toast should launch with the updated details | On clicking the update button, the following updates: the quantity, the subtotal, bag total, grand total and any delivery costs associated. A toast launches with the updated details
Bag | Bin button works | On clicking the bin button, the item is removed from the shopping bag and updates the total costs. The bag reloads with the updated items, and if removing that item takes the products to zero, a message should show that there are no items in the bag | On clicking the bin button, the item is removed from the shopping bag and updates the total costs. The bag reloads with the updated items, and if removing that item takes the products to zero, a message should show that there are no items in the bag
Bag | Keep Shopping and Secure Checkout buttons work | The "Keep Shopping" button should return the user to the product catalog, the "Secure Checkout" should send the user onto the checkout page | The "Keep Shopping" button returns the user to the product catalog, the "Secure Checkout" sends the user onto the checkout page

#### Checkout
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Checkout | Checkout page renders and is responsive | Checkout page should render and be responsive to devices. On mobile, the forms should render into one column with the order summary on the top, and the checkout form underneath, followed by the adjust bag and the complete order button. On desktops, the page should stretch out into two columns, with the order summary on the right hand side and the checkout form on the left with the buttons underneath the order form | Checkout page renders and is responsive to devices. On mobile, the forms render into one column with the order summary on the top, and the checkout form underneath, followed by the adjust bag and the complete order button. On desktops, the page stretches out into two columns, with the order summary on the right hand side and the checkout form on the left with the buttons underneath the order form
Checkout | Form is validating | Order should not be processed if the required fields are unfilled | Orders should not be processed if required fields are not filled in | Orders are not processed if the required fields are not filled in. The tooltip does not appear when anything is left unfilled on the Your Details section, however a tooltip does appear when anything is left unfilled on the Delivery section. This is a similar issue that showed up on the Kytchen Table project with the tooltips not appearing on Google Chrome on certain fields
Checkout | Payment Element is validating | Order should not be processed if the element is left unfilled. If the number is filled incorrectly, a Stripe relevant message should triggered which is determined by Stripe. | Orders are not processed if the element is left unfilled. If the number is filled incorrectly, a Stripe relevant message is triggered which is determined by Stripe
Checkout | Save this information checkbox | Save this information checkbox should only show for those who are logged into an account. If the tickbox is ticked, the information should be saved to the session and used to populate the profile delivery details | Save this information checkbox only shows for those who are logged into an account. If the tickbox is ticked, the information is saved to the session and used to populate the profile delivery details
Checkout | Delivery information populated | Delivery information that has been saved from a previous session should automatically populate if the user is logged in at the time they reach the checkout | Delivery information that has been saved from a previous session is automatically populated if the user is logged in at the time they reach the checkout
Checkout | "Adjust Bag" works | The "Adjust Bag" button should send the user back to their bag | The "Adjust Bag" button sends the user back to their bag
Checkout | "Complete Order" works | The "Complete Order" button should trigger the Stripe elements API which checks the information is correct and valid. If the information is valid, the checkout order success page should load. Whilst the order is being processed, a spinner should appear on the button powered by JavaScript | The "Complete Order" button triggers the Stripe elements API which checks the information is correct and valid. If the information is valid, the checkout order success page loads. Whilst the order is being processed, a spinner appears on the button powered by JavaScript

### Checkout Confirmation
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Checkout Confirmation | Checkout Confirmation renders | Checkout confirmation should render, showing the following information: the order number, the order date, a summary of the order, the delivery details and the billing information. Underneath two buttons should render - one for "Continue Shopping" and one for "Back to Profile" | Checkout confirmation should render, showing the following information: the order number, the order date, a summary of the order, the delivery details and the billing information. Underneath two buttons should render - one for "Continue Shopping" and one for "Back to Profile"
Checkout Confirmation | "Continue Shopping" button | "Continue Shopping button should return users to the products catalog | "Continue Shopping" button returns users to the product catalog
Checkout Confirmation | "Back to Profile" button | "Back to Profile" button should send users to the users individual profile | "Back to Profile" button sends users to their individual profile

#### Profile
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Profile | Profile renders and is responsive to device | Profile page renders and should appear be responsive to devices. On mobiles, the profile should stack, with the profile picture at the top, the delivery details underneath, and the order history below that. On tablets and above, the profile should stretch out so that the profile picture sits  in a singular row, and then the default delivery and order history sit in the same row in two separate columns. A button to update delivery details should show underneath the default delivery details | Profile page renders and is responsive to devices. On mobiles, the profile stacks, with the profile picture at the top, the delivery details underneath, and the order history below that. On tablets and above, the profile stretches out so that the profile picture sits  in a singular row, and then the default delivery and order history sit in the same row in two separate columns. A button to update delivery details should show underneath the default delivery details 
Profile | Default Profile Picture | Default profile picture should automatically attach to an account, and should show if the user removes their current profile picture | Default profile picture automatically attaches to an account, and shows if the user removes their current profile picture
Profile | Profile Picture can be updated | Users should be able to select a photo and upload to their profile. By clicking "choose file" it should launch a window with their own files. The user can choose whatever photo they like and on clicking "upload", the profile picture should attach to the profile and render at the top of the account | Users are able to select a photo and upload to their profile. By clicking "choose file" they launch a window with their own files. The user can choose whatever photo they like and on clicking "upload", the profile picture is attached to the profile and renders at the top of the account
Profile | Default Delivery Information renders | The default delivery should render in a form, which should be prepopulated with the information provided by the user from their delivery. If the user has not made any orders, this form should appear blank | The default delivery renders in a form, which is prepopulated with the information provided by the user from their delivery. If the user has not made any orders, this form appears blank
Profile | "Update Information" button working | If the user makes any changes to their delivery information and clicks "Update Information" then the page should reload with the updated information. The next time a user makes an order, the populated information in the order form should match the changes made. There has been no validation added to the profile form, so if the user chooses to leave empty fields they are should be able to save the form |  If the user makes any changes to their delivery information and clicks "Update Information" then the page reloads with the updated information. The next time a user makes an order, the populated information in the order form matches the changes made. There has been no validation added to the profile form, so if the user chooses to leave empty fields they are are be able to save the form
Profile | Order number links correctly | Order number should link to the correct previous order | Order number links to the correct previous order 
Profile | Order History shows correct information | Order History should render with the following information: date, items, total. This information should match the information shown in the Django Admin panel. The order history should move to a scroll once a user makes a certain amount of orders | Order History renders with the following information: date, items, total. This information matches the information shown in the Django Admin panel. The order history moves to a scroll once a user makes a certain amount of orders

#### AllAuth
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
AllAuth - Sign Up | AllAuth form | AllAuth form loads, asking user to provide a mandatory username, email and password. If the user tries to submit the form without providing this information, they should be prompted to fill in the required fields | AllAuth form loads, asking user to provide a mandatory username, email and password. If the user tries to submit the form without providing this information, they should be prompted to fill in the required fields
AllAuth - Sign Up | Verification Email | Verification email should be triggered once the user signs up and send to the email provided at sign up | Verification email is triggered once the user signs up and sends to the email provided at sign up. 
AllAuth - Sign Up | Verification Page | Once the user has clicked the link sent in their verification email, they should be taken to a verification page where they are asked to further confirm their verification. Once this has been verified they should be taken to the Sign In page | Once the user has clicked the link sent in their verification email, they are taken to a verification page where they are asked to further confirm their verification. Once this has been verified they are taken to the Sign In page
AllAuth - Sign Up | Redirect to Sign In works | If the user clicks on the hyperlinked "Sign Up here" they should be redirected to the Sign Up page | If the user clicks on the hyperlinked "Sign Up here" they are redirected to the Sign Up page.
AllAuth - Sign In | Standard Sign In | AllAuth form should load, asking user to provide mandatory username and password. If the user tries to log in without providing this information they should be prompted to fill in the required fields. If the information is correct, the user should be signed in and taken to the home page. If the information is incorrect, the user should be informed and asked to try again | AllAuth form loads, asking user to provide mandatory username and password. If the user tries to log in without providing this information they are prompted to fill in the required fields. If the information is correct, the user is signed in and taken to the home page. If the information is incorrect, the user is informed and asked to try again
AllAuth - Sign In | Facebook Sign In | If the user clicks "Continue with Facebook" they should be taken to a new page which warns them they are directing away from the site to log in through Facebook. On clicking "Continue" they should be taken to the Facebook AllAuth portal, and the user is able to choose who they wish which account they sign in with. On clicking the account, they should be redirected to the create account through 3rd party part of AllAuth and the user creates login credentials. Upon these being created, the user should be redirected to the home page | If the user clicks "Continue with Facebook" they are be taken to a new page which warns them they are directing away from the site to log in through Google. On clicking "Continue" they are taken to the Facebook AllAuth portal, and the user is able to choose who they wish which account they sign in with. On clicking the account, they are redirected to the create account through 3rd party part of AllAuth and the user creates login credentials. Upon these being created, the user is redirected to the home page
AllAuth - Sign In | Facebook Sign In | "Cancel and Go Back" button works | Clicking the "Cancel and Go Back" button should return the user to the general AllAuth Sign In page | Clicking the "Cancel and Go Back" button returs the user to the general AllAuth Sign In page
AllAuth - Sign In | Google Sign In | If the user clicks "Continue with Google" they should be taken to a new page which warns them they are directing away from the site to log in through Google. On clicking "Continue" they should be taken to the Google AllAuth portal, and the user is able to choose who they wish which account they sign in with. On clicking the account, they should be redirected to the home page and an account is created associated to that account if they have not signed in on that email before | If the user clicks "Continue with Google" they are be taken to a new page which warns them they are directing away from the site to log in through Google. On clicking "Continue" they are taken to the Google AllAuth portal, and the user is able to choose who they wish which account they sign in with. On clicking the account, they are redirected to the home page and an account is created associated to that account if they have not signed in on that email before 
AllAuth - Sign In | Google Sign In | "Cancel and Go Back" button works | Clicking the "Cancel and Go Back" button should return the user to the general AllAuth Sign In page | Clicking the "Cancel and Go Back" button returs the user to the general AllAuth Sign In page
AllAuth - Sign Out | Sign Out button | Sign out button should successfully sign out the user, redirecting them to the homepage. | Sign out button successfully signs out the user, redirecting them to the homepage. 

#### Additional Pages
| Feature Tested | Action | Expected Result | Actual Result
--- | --- | --- | ---
Our Story | Our Story page renders | Our Story page should render and shows the full biography | Our Story page renders and shows the full biography
FAQ | FAQ page renders | FAQ page should render and show the full paragraph and accordion | FAQ page renders and shows the full paragraph and accordion
FAQ | FAQ Accordion | The FAQ accordion should activate when a user clicks the accordion bar. The accordions should be able to be opened independently and closed independently rather than opening and closing together | The FAQ accordion activates when a user clicks the accordion bar. The accordions are able to be opened independently and closed independently rather than opening and closing together
Privacy Policy | Privacy Policy renders | The Privacy Polucy should render and show the full policy | The Privacy Polucy renders and show the full policy
Contact Us | Contact Us renders | Contact Us page should render with the form showing for users to fill in | Contact Us page should render with the form showing for users to fill in
Contact Us | Validation works | Contact Us form should be filled in on all fields. If any fields are not filled, the user should be prompted where they need to fill the form. The form should not be able to be submitted until validation has been satisfied | Contact Us form must be filled in on all fields. If any fields are not filled, the user is prompted where they need to fill the form. The user is unable to submit until validation has been satisfied
Contact Us | Message is recieved by Django Admin | Contact Us message should be accessible via the Django Admin panel | Contact Us message is accessible via the Django Admin panel
Shipping | Shipping renders | Shipping should render and show all information | Shipping renders and show all information
Returns | Returns renders | Returns should render and show all information | Returns renders and show all information


### Automated Unit Testing
Due to project time constraints and prioritising production stability, automated unit tests were not implemented for this version of the project. The priority was ensuring core functionality — including payments, media storage, and deployment stability — was fully working in production. Instead, I relied on thorough manual testing across different devices and environments, carefully checking key user flows such as account creation, checkout, order confirmation, and admin functionality. While automated tests would have strengthened the project further, particularly for long-term maintainability, the focus at this stage was on delivering a stable, fully functioning live application within the available timeframe.

### Testing Against User Stories
| User Story | Category (MoSCoW) | Met?
--- | --- | --- 
As a user of the website, I want to be able to browse products so that I can find items to purchase | Must Have | Met
As a user of the website, I want to be able to view product details for each individual product, so that I can understand if the product is suited for my needs | Must Have | Met
As a staff member (Admin role), I want to be able to add, amend and delete products from the website | Must Have | Met
As a user, I can sign up to become a registered user, so that I can track have a profile that tracks previous orders and automatically populate fields with my details at checkout | Must Have | Met
As a user, I will receive a confirmation email when I have created an account, so that I can securely validate my account | Must Have | Met
As a registered user I am able to securely log in and log out of my profile so that I know that my account is safe | Must Have | Met
As a user of the website, I can add items to a shopping bag and see how much the grand total is, so that I can track how much I am spending | Must Have | Met
As a user of the website, I can change the quantity of the items in my shopping bag and an updated grand total, so that I can track how much I am spending | Must Have | Met
As a user of the website I can remove items from my shopping bag and see an updated grand total, so that I can remove items I do not need anymore | Must Have | Met
As a user of the website I can be shown all the items I am buying, plus the subtotal, shipping details and grand total before I complete the purchase, so that I can decide that I definitely want to complete the purchase | Must Have | Met
As a user of the website I can enter my details into the checkout securely, using the Stripe API, so that I can purchase items safely and securely | Must Have | Met
As a user, I want to be able to sign up to The Tavern's newsletter, so I can learn about their community | Must Have | Met
As a user of the website, I want to be able to read product reviews, so that I can see how other people have experienced the item and decide if it suits my needs | Should Have | Met
As a registered user of the website, I want to be able to leave product reviews, so that I can help inform other potential buyers about my opinion of the product | Should Have | Met
As a staff member (Admin role), I want to be able to approve product reviews, so that I can ensure that only quality reviews end up on the website | Should Have | Met
As a staff member (Admin role), I want to be able to delete product reviews, so that I can ensure that inappropriate reviews do not end up on the website | Should Have | Met
As a registered user, I am able to update my profile information, so that I can be sure that my details are up to date | Should Have | Met
As a registered user, I am able to reset my password at any time, so that I can keep my account secure | Should Have | Met, through Allauth but only on the sign in page rather than as an intended button on the profile
As a registered user, I am able to see my previous orders, so that I can track any orders I have made in the past | Should Have | Met
As a user of the website, I can be shown my order details once my order is confirmed, so that I can see that my order has been completed | Should Have | Met
As a user of the website, I can receive an email confirming my order once my order has been successfully submitted | Should Have | Met
As a user, I want to be able to contact the team behind The Tavern, so I can know that I can message directly with questions, queries or suggestions | Should Have | Met
As a registered user, I am able to give myself a profile picture, so that I can have a photo on my profile | Could Have | Met
As a user, I want to be able to see information about the company, so I can know who I'm buying from | Could Have | Met
As a staff member (Admin role) I want to be able to update the information on the company, so that I can keep this up to date as the company grows and expands | Could Have | Met

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

### Marketing Strategies
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

### Social Media
As part of the project, I created a Facebook page for The Tavern, which the team can use to launch products, engage with customers and build on the brand. This approach aligns with the needs of the TTRPG audience, which is increasingly a wide spread age group from the very young, to the very young at heart! Facebook is traditionally a market for older audiences, typically 40+ and acts as a bridge to get customers from their social media platform, over to the website itself. Please see a screenshot of the Facebook page below. Please note that due to Meta's careful monitoring of pages to ensure that they are active and accurate, the page may be subject to removal by Meta if flagged as non-authentic or not meeting platform verification requirements.

![Facebook Page for The Tavern](https://github.com/foster95/the_tavern/blob/main/documentation/brand/facebook-page-01.png)

Were the project be to developed further, I would strongly suggest that The Tavern move to launch platforms on TikTok and Instagram, which is why those two platforms have been linked in the footer. As TTRPGs grow in media presence due to platforms like Critical Roll and Dimension 20, the audience is getting younger and tech savvier, and these platforms are better suited to that environment. TikTok and Instagram work more with short content often called "reels", which capture an audience that is increasingly scrolling on the go. I would suggest that the company focus on building a sense of community within these platforms, offering followers tips, tricks and suggestions for them to incorporate into their home campaign, rather than solely focussing on using social media as a further tool to sell the product. Customers are increasingly suspicious of a company just selling to them, and therefore becoming a expert and trusted source for TTRPG information will build the trust that will make it easier to bridge that gap from follower to purchaser. 

### Email Marketing
Within the project I have implemented a mailing list sign up which sits just above the footer and appears on every page. This will allow the team at The Tavern to create and build a newsletter community and create brand awareness. As the project only required me to create the newsletter, I have gone no further in developing this. However, if the team were to further develop this, I would encourage a weekly newsletter, which includes promotions, however I would strongly advise against using the email marketing tool as a pure sales tool. Again, I would suggest that The Tavern work to build a community, so the newsletter becomes a helpful source of tips and tricks for improving gameplay as well as fun "race/class of the month", then it will be much easier to drip feed in some occasional product launches, rather than just inundating users with promotions and products. 

## Deployment 
This project has been developed using Django and deployed to Heroku, using PostgreSQL for the backend database and AWS S3 for static and media file storage. The static and media files are hosted on AWS S3 for efficient delivery. The deployment process involves several steps, including setting up the Heroku app, configuring environment variables, and ensuring that all dependencies are properly managed.

The following steps describe how another developer can recreate the project locally and deploy it to Heroku:

### Fork 
Forking creates your own copy of the project repository on GitHub, allowing you to make changes without affecting the original project.

1. Log in to your GitHub account.
2. Navigate to the repository page.
3. Click the Fork button in the upper right corner of the page.
4. Select your GitHub account as the destination for the fork.

### Clone
Cloning the repository downloads a copy of the project to your local machine, allowing you to work on it offline.

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the project.
3. Run the following command, replacing your-username with your GitHub username:

            git clone https://github.com/your-username/your-repo
            cd -

### Create and Activate a Virtual Environment:
A virtual environment isolates your project's dependencies from other Python projects on your machine.

1. Create the virtual environment with the following command:

            python3 -m venv venv

2. To activate or relaunch the venv:
On macOS/Linux:

            source venv/bin/activate

On Windows:
            venv\Scripts\activate

### Install Dependencies
Install the required Python packages listed in the requirements.txt file:

            pip install -r requirements.txt

If requirements.txt is not present, you can create it by running:

            pip freeze > requirements.txt

### Set Up a Local Environment File
Sensitive information such as API keys and database credentials should not be hardcoded in the codebase. Instead, they should be stored in environment variables which are not committed to Github.

Create a .env file in the root directory of the project to store environment variables securely. Add the following variables, replacing the placeholder values with your own:

| Key | Value
--- | ---
DATABASE_URL | user-inserts-own-postgres-database-url
DISABLE_COLLECTSTATIC | 1 (this is temporary, and can be removed for the final deployment)
EMAIL_HOST_PASS | user-inserts-own-gmail-api-key
EMAIL_HOST_USER | user-inserts-own-gmail-email-address
SECRET_KEY | any-random-secret-key
STRIPE_PUBLIC_KEY | user-inserts-own-stripe-public-key
STRIPE_SECRET_KEY | user-inserts-own-stripe-secret-key
STRIPE_WH_SECRET | user-inserts-own-stripe-webhook-secret
AWS_ACCESS_KEY_ID | user-inserts-aws-access-key-id
AWS_SECRET_ACCESS_KEY | user-inserts-aws-access-secret-key-id

<strong>Do not commit the .env file to version control. Add it to your .gitignore file to prevent accidental exposure of sensitive information.</strong>

### Data Migrations
1. Apply database migrations

            python3 manage.py migrate

2. If using fixtures, load them into the database (optional)

            python3 manage.py loaddata your_fixture_file.json

3. Create a superuser account for accessing the Django admin

            python3 manage.py createsuperuser

### Run Development Server
Start the Django development server to test the application locally:

            python3 manage.py runserver

Open web browser and navigate to http://127.0.0.1:8000/ to view the application.

### Set up AWS S3 for Static and Media Files
1. Create an AWS account if you don't already have one.
set up an S3 bucket for storing static and media files.
2. Choose a unique name for your bucket and select the appropriate region.
3. Make sure the uncheck "Block all public access" option to allow public read access to your files.
4. Enable static webhosting on the bucket.
5. Permission - Add a bucket policy to allow public read access to objects in the bucket. 
6. Create an IAM user with programmatic access and attach a policy that grants the necessary permissions to access the S3 bucket:
    1. Go to IAM → Users → Add users.
    2. Create a user
    3. Enable programmatic access
    4. Attach a policy which allows S3 access to your bucket.
    5. Save the Access Key ID and Secret Access Key for use in your .env file. These will also be added to Heroku Config Vars later.
    6. Update the .env file with your AWS credentials and bucket information

### Prepare for Deployment:
1. Install Gunicorn, a production-ready web server:

            pip install gunicorn

2. Update requirements.txt:

            pip freeze > requirements.txt

3. Create a Procfile in the root directory with the following content:

            web: gunicorn the_tavern.wsgi:application

4. Update Django settings for production, including allowed hosts and static file handling.

* Debug disabled in production

            DEBUG = False

* Set allowed hosts

            ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost', '127.0.0.1']

* Static configurations for collectstatic

            STATIC_URL = '/static/'
            STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

* Configure AWS S3 storage settings for when enabled.

            if USE_AWS in os.environ:
                # AWS S3 settings here

### Deploy to Heroku
1. Log in to your Heroku account and create a new app - New → Create new app.
2. Name the app (must be unique) and select your region.
3. Go to resources tab and add the Heroku Postgres add-on for the database. Heroku will automatically set the DATABASE_URL environment variable.
4. Go to the Settings tab and click on Reveal Config Vars. Add the environment variables from your .env file

| Key | Value
--- | ---
DATABASE_URL | user-inserts-own-postgres-database-url
DISABLE_COLLECTSTATIC | 1 (this is temporary, and can be removed for the final deployment)
EMAIL_HOST_PASS | user-inserts-own-gmail-api-key
EMAIL_HOST_USER | user-inserts-own-gmail-email-address
SECRET_KEY | any-random-secret-key
STRIPE_PUBLIC_KEY | user-inserts-own-stripe-public-key
STRIPE_SECRET_KEY | user-inserts-own-stripe-secret-key
STRIPE_WH_SECRET | user-inserts-own-stripe-webhook-secret
AWS_ACCESS_KEY_ID | user-inserts-aws-access-key-id
AWS_SECRET_ACCESS_KEY | user-inserts-aws-access-secret-key-id

1. Go to the Deploy tab, select GitHub as the deployment method, and connect your GitHub repository.
2. Choose the branch to deploy (usually main or master) and click Deploy Branch.
3. After deployment, run database migrations on Heroku:

            heroku run python3 manage.py migrate --app your-heroku-app-name

4. Create a superuser on Heroku

            heroku run python3 manage.py createsuperuser --app your-heroku-app-name

5. Open your deployed application in the browser: ```bash heroku open --app your-heroku-app-name

You have now successfully deployed to Heroku!

## Tools and Technologies
### Media and Design
* Google Gemini - Product images and product copy 
* Coolors - Colour Palettes
* Our Own Thing - Font pairing website
* Google Fonts - Fonts across the full website
* Canva - Wireframes
* Online Convert - Convert images from jpg to webp
* Compress or Die - Webp compressor

### Database
* Miro - ERD creation
* Mailchimp - Newsletter sign up database

## Debugging and Testing
* ChatGPT - General Debugging Assistance
* W3C HTML Validation - HTML Validation
* W3C CSS Validation - CSS Validation
* JShint - JavaScript Validation
* Lighthouse - Performance Checker
* WAVE from WebAim - Accessibility Checker
* Blisk - Device Compatability Checker 