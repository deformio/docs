# CLI Reference

Deform command line client (CLI) allows you talk to and operate Deform using the command line interface. It talks to the Deform using the public API.

## Installation

    $ pip install python-deform

## Configuration

## Usage

CLI

deform user
deform register
deform login
deform auth-by-token
deform logout
deform confirm

deform projects

deform use-project <project-id>
deform project [get|update] <project-id>

deform collections [find]
    --project <project_id>
    [--query <query>]
    --fields <field1,field2>
    --exclude-fields <field1,field2>

deform collection [get|save|create|update|remove] <collection_id>
    --project <project_id>
    [--property <path.to.property>]
    --fields <field1,field2>
    --exclude-fields <field1,field2>

deform documents [find|update|upsert|remove]
    --project <project_id>
    --collection <collection_id>
    [--query <query>]
    [--data <data>]
    --fields <field1,field2>
    --exclude-fields <field1,field2>

deform document [get|save|create|update|remove] <document_id>
    --project <project_id>
    --collection <collection_id>
    [--property <path.to.property>]
    --fields <field1,field2>
    --exclude-fields <field1,field2>
