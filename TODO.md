# TODO: Enable Admin to Manage Team Department in About Page

## Step 1: Create TeamMember Model ✅
- Add TeamMember model to printerapp/models.py with fields: name, position, email, image, department (choice field with Office Printer, Solar, IT)

## Step 2: Register Model in Admin ✅
- Register TeamMember in printerapp/admin.py

## Step 3: Create Form ✅
- Add TeamMemberForm to dashboard/forms.py

## Step 4: Add CRUD Views ✅
- Add team_list, team_add, team_edit, team_delete views to dashboard/views.py

## Step 5: Add URLs ✅
- Add team URLs to dashboard/urls.py

## Step 6: Create Templates ✅
- Create team_list.html
- Create team_form.html
- Create team_confirm_delete.html in dashboard/templates/dashboard/

## Step 7: Update Dashboard Home ✅
- Add team management link and count to dashboard/templates/dashboard/home.html

## Step 8: Update About Page ✅
- Modify uoas/templates/about.html to display team members dynamically, grouped by department

## Step 9: Update About View ✅
- Modify uoas/views.py to pass team data to about template

## Step 10: Run Migrations ✅
- Execute makemigrations and migrate

## Step 11: Test
- Test dashboard team management
- Test about page display
