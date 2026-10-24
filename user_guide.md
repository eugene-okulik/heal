# User Guide: Ecommerce Store

Welcome to the Ecommerce Store user guide. This document explains how to use all customer-facing features of our online store.

## Table of Contents
- [Getting Started](#getting-started)
- [Browsing Products](#browsing-products)
- [Shopping Cart](#shopping-cart)
- [User Accounts](#user-accounts)
- [Placing Orders](#placing-orders)
- [Order History](#order-history)
- [Tips & Troubleshooting](#tips--troubleshooting)

## Getting Started

### Accessing the Store
Open your web browser and navigate to:
```
http://localhost:8000
```
(or your domain if deployed)

### Navigation Overview
The main navigation bar at the top includes:
- **Home**: Returns to the store homepage
- **Products**: Browse all available products
- **Login/Register**: Access your account or create a new one
- **Cart**: View and manage your shopping cart (shows item count)

## Browsing Products

### Homepage
The homepage displays:
- Featured products (highlighted items)
- Navigation to browse by category
- Store branding and information

### Product Listing Page
Accessible via the "Products" link in navigation:
- **Grid View**: Products displayed in a responsive grid
- **Product Cards**: Each shows:
  - Product image (or placeholder)
  - Product name
  - Short description
  - Price
  - Availability status
  - "View Details" button
- **Category Filtering**: Click category links in the sidebar to filter products
- **Pagination**: Navigate through multiple pages of results

### Product Detail Page
Click any product to view detailed information:
- **Image Gallery**: Main image with thumbnail navigation (if multiple images available)
- **Product Information**:
  - Product name
  - Price
  - Availability status (In Stock/Out of Stock)
  - Stock quantity (when available)
  - Detailed description
  - Category assignment
- **Add to Cart Form**:
  - Quantity selector (minimum 1, maximum available stock)
  - "Add to Cart" button
- **Related Products**: Suggestions for similar items at the bottom

## Shopping Cart

### Accessing Your Cart
- Click the shopping cart icon in the navigation bar
- Or visit `/cart/` directly
- The cart icon shows a badge with the number of items

### Cart Page Layout
Your cart displays:
- **Order Summary Table**:
  - Product thumbnail and name
  - Unit price
  - Quantity selector with update buttons
  - Line total (price × quantity)
  - Remove item button (trash icon)
- **Order Totals**:
  - Subtotal
  - (Taxes and shipping would be calculated here in a production implementation)
  - Total amount
- **Action Buttons**:
  - "Continue Shopping": Returns to product browsing
  - "Proceed to Checkout": Begins order process

### Managing Cart Items
#### Changing Quantities
1. Locate the quantity input field for an item
2. Enter a new quantity (must be at least 1)
3. Click the "Update" button (or press Enter)
4. The line total and order totals will update automatically
5. If quantity exceeds available stock, you'll see an error message

#### Removing Items
1. Click the trash icon (��✕) next to any item
2. Confirm the removal when prompted
3. The item will be removed and totals updated

#### Special Cart Notes
- **Anonymous Users**: Cart is preserved for the duration of your browser session (via cookies)
- **Authenticated Users**: Cart is saved to your account and persists across devices/sessions
- **Merging Carts**: If you add items anonymously then log in, your carts will be merged
- **Stock Validation**: The system prevents adding more items than are in stock

## User Accounts

### Creating an Account
1. Click "Register" in the navigation bar
2. Fill in the registration form:
   - **Username**: Unique identifier for login
   - **Email**: Valid email address (used for communications)
   - **Password**: Secure password (minimum 8 characters recommended)
   - **Confirm Password**: Repeat password for verification
3. Click "Register" button
4. You'll be automatically logged in and redirected to the homepage
5. A welcome message will confirm successful registration

### Logging In
1. Click "Login" in the navigation bar
2. Enter your:
   - Username or Email
   - Password
3. Click "Login" button
4. If credentials are correct, you'll be redirected to your intended page or homepage
5. A welcome message will confirm successful login

### Logging Out
1. Click "Logout" in the navigation bar
2. You'll be signed out and redirected to the homepage
3. A confirmation message will indicate successful logout

### Managing Your Profile
Accessible via `/accounts/profile/` when logged in:

#### Account Information Section
- **First Name**: Your given name
- **Last Name**: Your family name
- **Email**: Your email address (display-only for security; contact support to change)
- *Note: Name fields are used for order shipping information*

#### Profile Details Section
- **Phone Number**: Contact telephone number
- **Address Line 1**: Primary street address
- **Address Line 2**: Additional address information (apartment, suite, etc.)
- **City**: City or town
- **State/Province**: State, province, or region
- **Postal/ZIP Code**: Postal code for mail delivery
- **Country**: Country of residence

#### Updating Your Profile
1. Modify any editable fields in the form
2. Click "Update Profile" button at the bottom
3. A success message will confirm your changes were saved
4. If validation fails, error messages will indicate what needs correction

### Account Security
- Passwords are securely hashed and never stored in plain text
- Use a unique password not used on other sites
- Consider using a password manager for generating and storing strong passwords
- Never share your login credentials with others

## Placing Orders

### Prerequisites
- At least one item in your shopping cart
- For best experience: be logged in (though checkout works as guest)

### Checkout Process

#### Step 1: Review Cart
- Verify items, quantities, and prices in your cart
- Use the cart page to make any final adjustments
- Click "Proceed to Checkout"

#### Step 2: Shipping Information
Fill in the checkout form with:
- **First Name*** (required): For shipping address
- **Last Name*** (required): For shipping address
- **Email Address*** (required): For order confirmation and communications
- **Phone Number**: Optional contact number
- **Address Line 1*** (required): Street address
- **Address Line 2**: Apartment, suite, unit, etc. (optional)
- **City*** (required): City or town
- **State/Province*** (required): State, province, or region
- **Postal/ZIP Code*** (required): Mailing code
- **Country*** (required): Defaults to United States but can be changed

*All fields marked with * are required

#### Step 3: Order Review
- The system displays an order summary showing:
  - List of items with quantities and totals
  - Order total amount
- Review all information for accuracy
- Check the checkbox agreeing to terms (if applicable)
- Click "Place Order" to submit

#### Step 4: Order Confirmation
Upon successful submission:
- You'll see an order confirmation page with:
  - **Order Number**: Unique identifier for your purchase
  - **Order Date**: When the order was placed
  - **Order Status**: Current status (typically "Pending" initially)
  - **Payment Status**: Payment status (typically "Pending" for COD or "Paid" for immediate payment)
  - **Shipping Address**: The address you provided
  - **Order Items**: Detailed list of what you purchased
  - **Total Amount**: Final cost of your order
- Options to:
  - Continue shopping
  - View order history (if logged in)
- An email confirmation will be sent to the address you provided

### Payment Note
This implementation simulates payment processing. In a production environment, this step would integrate with a payment gateway like Stripe, PayPal, or similar service to securely process credit card payments.

## Order History

### Accessing Order History
- Must be logged in to view order history
- Navigate to `/orders/history/` or click "View Order History" from your profile page
- Alternatively, access from order confirmation page after placing an order

### Order History Page Layout
Displays a table of all your orders with:
- **Order Number**: Unique identifier (click to view details)
- **Order Date**: When the order was placed
- **Order Status**: Current fulfillment status
- **Payment Status**: Payment processing status
- **Total Amount**: Order total cost
- **Action**: "View Details" button for each order

### Order Detail Page
When viewing a specific order:
- **Order Information**:
  - Order number and date
  - Current order and payment statuses (with colored badges)
- **Shipping Address**: The destination address for the order
- **Order Items Table**:
  - Product name and thumbnail
  - Unit price
  - Quantity ordered
  - Line total
- **Order Total**: Final amount paid
- **Navigation**:
  - Button to return to order history
  - Button to continue shopping
  - Button to return to homepage

### Order Status Meanings
- **Pending**: Order received, not yet processed
- **Processing**: Order being prepared for shipment
- **Shipped**: Order has left the warehouse/facility
- **Delivered**: Order received by customer
- **Cancelled**: Order was cancelled (by customer or system)

### Payment Status Meanings
- **Pending**: Payment not yet processed or received
- **Paid**: Payment successfully received
- **Failed**: Payment attempt was unsuccessful
- **Refunded**: Payment was returned to customer

## Tips & Troubleshooting

### Best Practices
1. **Create an Account**: While you can shop as a guest, having an account provides:
   - Order history tracking
   - Saved address information for faster checkout
   - Wishlist capabilities (in future updates)
   - Faster login on return visits

2. **Keep Your Cart Updated**: Before checkout, review quantities to ensure you want exactly what's in your cart

3. **Use Secure Connections**: Always ensure you're on a secure network when entering personal information

4. **Save Order Numbers**: Keep your order number for reference when checking status or contacting support

### Common Issues and Solutions

#### "Item out of stock" Error
- **Cause**: Trying to purchase more items than available in inventory
- **Solution**: Reduce quantity to available stock or select a different product

#### "Session expired" or Cart Losing Items
- **Cause**: Browser cookies cleared or session timeout
- **Solution**: 
  - Log in to associate cart with your account
  - Avoid clearing browser cookies while shopping
  - Complete purchase in a reasonable timeframe

#### Login Problems
- **Incorrect Password**: Use the "Forgot password" feature (if implemented) or reset via admin
- **Username Not Found**: Verify you're using the correct username or try your email address
- **Account Locked**: Contact administrator if too many failed attempts

#### Checkout Issues
- **Missing Required Information**: All fields marked with * are required
- **Invalid Email Format**: Ensure you enter a valid email address (name@domain.com)
- **Address Validation**: Some special characters in addresses may cause issues; use standard alphanumeric format where possible

#### Display or Layout Problems
- **Browser Compatibility**: Tested on modern browsers (Chrome, Firefox, Safari, Edge)
- **Zoom Level**: Ensure browser zoom is at 100% for proper layout
- **Screen Size**: Responsive design works down to 320px width (mobile phones)

### Getting Help
If you encounter issues not covered here:
1. Check that you're using the latest version of your browser
2. Clear your browser cache and reload the page
3. Try accessing the store in an incognito/private browsing window
4. Contact customer support with:
   - Detailed description of the problem
   - Steps to reproduce the issue
   - Screenshots if possible
   - Time and date when the issue occurred
   - Any error messages shown

### Accessibility Features
The store aims to be accessible with:
- Semantic HTML structure
- ARIA labels where needed
- Keyboard navigable interface
- Sufficient color contrast
- Resizable text without breaking layout
- Form labels associated with inputs

## Conclusion

Thank you for choosing our Ecommerce Store! This user guide covers all customer-facing features to help you make the most of your shopping experience. Remember that your feedback helps us improve, so don't hesitate to reach out with suggestions or report any issues you encounter.

Happy shopping!