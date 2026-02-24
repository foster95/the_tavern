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

## Databse Design
### Data Models
Prior to building The Tavern, I created an ERD which helped me visualise all of the relationships between the different datasets and databases in the site. I used Miro to create this:

## Website Features
### Header
The header extends the base.html template, and is a simple, minimalistic design which is visually appealing for users. On mobile the header is much simpler, displaying only the most crucial features of the website to allow users easy UX - these features are: a drop down burger icon which allows users to navigate to the following: all products, dice, other accessories, about us, FAQ and contact us. There is also a search button, allowing users to search the site, a my account button, and a basket button. On tablets and up, the header is much more elaborate, featuring a small version of the companies logo on the left hand side, a central search bar and the account and basket features on the right hand side of the screen. Running just below this in a seperate bar is the product catalogue, and seperated from this the FAQ and the contact us button can be found in the header. This allows users to easily navigate to the product directory, but requires them to search a little further for the other pages, which is the ultimate goal of an eCommerce site. 

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

## Testing
### Summary of Testing


### Lighthouse
| Page | Format | Lighthouse Grades
--- | --- | --- 
Home | Desktop | 
Home | Mobile | 
Products | Desktop | 
Products | Mobile | 0%
Product Details | Desktop | 
Product Details | Mobile | 
Add Product | Desktop | 
Add Product | Mobile | 
Amend Product | Desktop | 
Amend Product | Mobile | 
Bag | Desktop | 
Bag | Mobile | 
Checkout | Desktop | 
Checkout | Mobile | 
Order Confirmation | Desktop | 
Order Confirmation | Mobile | 
Profile | Desktop | 
Profile | Mobile | 
Contact | Desktop | 
Contact | Mobile | 
About | Desktop | 
About | Mobile | 
FAQ | Desktop | 
FAQ | Mobile | 
Privacy | Desktop | 
Privacy | Mobile | 
Returns | Desktop | 
Returns | Mobile | 
Shipping | Desktop | 
Shipping | Mobile | 
Sign In | Dekstop |
Sing In | Mobile |
Sign Out | Desktop
Sign Out | Mobile
Sign Up | Desktop
Sign Up | Mobile 

### HTML Validation
| Page | Report | Notes
--- | --- |---
Home |  |
Products | | 
Product Details | |
Add Product | |
Amend Product | | 
Bag | |
Checkout | |
Order Confirmation | |
Profile | |
Contact | |
About | |
FAQ | |
Privacy | |
Returns | |
Shipping | |

### PEP8 Validation
#### Home
| File | PEP8 Response
--- | ---
Admin | 
Apps |
Models |
URLs |
Views |

#### Products
| File | PEP8 Response
--- | ---
Admin | 
Apps |
Forms |
Models |
URLs |
Views |

#### Bag
| File | PEP8 Response
--- | ---
Admin | 
Apps |
Contexts |
Models |
URLs |
Views |

#### Checkout
| File | PEP8 Response
--- | ---
Admin | 
Apps |
Forms |
Models |
Signals |
URLs |
Views |
Webhook-Handler |
Webhooks

#### Profiles
| File | PEP8 Response
--- | ---
Admin | 
Apps |
Models |
Forms |
URLs |
Views |

### JShint
| File | JShint
--- | ---
newsletter.js | 
bag.js |
stripe_elements.js |
product_details.js |
product_form.js |
product_review.js |
products.js |
profile.js |







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
* Online Convert - Convert images from jpg to webp
* Compress or Die - Webp compressor

### Database
* Miro - ERD creation
* Mailchimp - Newsletter sign up database

## Debugging and Testing
* ChatGPT
* W3C HTML Validation
* W3C CSS Validation
* JShint
* Lighthouse