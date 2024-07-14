

## postgres migration
* create migrations file
    ```shell
    cd src && alembic revision --autogenerate
    ```  
  this will create a new file in src/orm/alembic/versions

* apply the migration
    ````shell
    alembic upgrade head
    ````
  after run this cmd, alembic will apply changes to Postgres, and create a new table named alembic_version, 
  if not exists. The table has a field named version_num.  
