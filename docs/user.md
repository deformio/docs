# User

## Registration

In order to use a service you will need to **register** with your email.

Registration contains two steps:

  * Use your email to signup
  * Confirm email using a code received

### Signup

Use a [CLI](/cli/) to register:

```bash
deform signup -e EMAIL -pPASSWORD
```

This will send you a unique code to proceed.

### Confirm

Now you need to confirm an email you used for [signup](/user/#signup). Use a `CONFIRMATION_CODE` received in an email we've sent you.

If you accidentally deleted or lost an email - signup again. We'll send you email with another code.

All codes we've sent you are valid to confirm. After confirmation they are no longer valid.

```bash
deform confirm CONFIRMATION_CODE
```

## Create first Project

Now you can create your first project.

```bash
deform project create -d '{"_id":"my-first-project", "name":"My First Project"}'
```

Use this project.

```bash
deform use-project my-first-project
```

Great, you've created a project :D
