# Hospital Management

## What is this?

This is a custom module tutorial for odoo 15.

## Step to start

1. Create odoo user.

```bash
sudo adduser -system -home=/opt/odoo -group odoo
```

2. Install PostgreSQL

```bash
sudo apt install postgresql
```

3. Create database user as `odoo` and change password also as `odoo`

```bash
sudo su postgres
psql
```

```sql
createuser
-s odoo
```

```sql
ALTER
USER odoo WITH PASSWORD 'odoo';
```

4. Install Python dependencies

```bash
sudo apt install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev
```

5. Install NodeJs

```bash
sudo apt install nodejs npm
```

6. Install Wkhtmltopdf
   Goto [this](https://wkhtmltopdf.org/downloads.html) site and download according to your environment and install it.
7. Create Log files

```bash
sudo mkdir /var/log/odoo
sudo chown odoo:odoo /var/log/odoo
```

8. Download Odoo

```bash
sudo apt install git
sudo git clone --depth 1 --branch 15.0 https://www.github.com/odoo/odoo ./odoo15
```

9. Set permissions to odoo files

```bash
sudo chown -R odoo:odoo odoo15/*
```

10. Odoo configurations
    Goto file `odoo15/debian/odoo.conf`.
    Make the changes as fallows

```conf
db_host = localhost
db_password = odoo  
db_port = 5432
addons_path= addons, custom_addons
```

11. Create virtual environment and Install dependencies

```bash
cd odoo15
python3 -m venv venv
pip install -r requirements.txt
```

12. Activate the environment

```bash
source venv/bin/activate
```

13. Start Odoo

```bash
python3 odoo-bin -c debian/odoo.conf
```

14. Goto web site
    Click [`http://localhost:8069/`](http://localhost:8069/)
    At first time setup admin credentials and database.

## Before start development, you should read fallowing...

- Technical name will be the folder name of the module.
- Primary configurations are in `__manifest__.py` file.
- In `__manifest__.py` file
    - name: Display name
    - version: Version of the module
    - sequence: Sort order
    - installable: Appear of the installation button
    - application: Appear under apps
    - data: All XML files should be defined here
- Should import all python files in `__init__.py`.
- Module icon is at `module_folder/static/description/icon.png`.
- Models are placed in `module_folder/models`.
- Menus
    - Menus are written in `module_folder/views/menu.xml` file.
    - There should be an action to visible the menu item.
    - Menu Item should be unique.
- Window Actions
    - Tag is `actionitem`
    - Written in XML file
- When calling XML files, there may be errors like not defined. It is because the item will load later. for be mindful
  with the flow of the components.
- When not adding any access writes, you can access items via being superuser. It is at debug icon on top right corner.
- To exit superuser you have to log out and login again.
- Security
  - Should be imported in `__manifest__.py` file. And security rules should be called at top most of the list.
  - All security related files should be placed in `module_folder/security` folder.
  - File should be named as model name of access right page. It is in the URL parameters. eg: `irr.model.access`.
- From Views
  - It is lot like a Window action.
  - Written in XML files.
  - `form` define the way of adding new item to table.
  - `<group> ... </group>` will give the labels. Otherwise, no labels, only input lags.
- Tree View
  - Same as form view.
  - `form` tag should be changed as `tree`.
  - field tag has attribute called string to change table name.
- Search View (Control Panel View)
  - For Search bar.
  - Keyword is `search`.
  - `filter_domain` attribute in `field` can be used to search advanced search like `OR` operator.
  - `filter` tag can be used to develop custom pre-defined filters.
  - Applying multiple filters with in separators combined with OR operator. Without same seperator combined with AND operator.
  - `<separator />` is the seperator tag that described above.
  - 