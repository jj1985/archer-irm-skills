# Archer Next Generation Risk Experience API (SaaS Clients Only)

On this page

  * Archer Next Generation Risk Experience API (SaaS Clients Only)
    * How do I access documentation for the NGRX APIs?
    * How do I access the NGRX APIs?
    * How do I use the JSON Web Token (JWT) to access NGRX APIs?
      * Step 1: Obtain your token
      * Step 2: Request your JWT
      * Step 3: Receive JWT and store for future use
      * Step 4: Use the JWT in future requests

## How do I access documentation for the NGRX APIs?

Documentation for the Next Generation Risk Experience (NGRX) APIs is available through the Swagger UI in your Archer environment. Use the following steps to access the API documentation:

  1. Log in to your non-production Archer environment.

  2. Replace everything after your Archer URL with `ngrx/record/swagger/index.html`.

**Note:** Swagger UI documentation for the NGRX APIs is currently available only in non-production environments.

## How do I access the NGRX APIs?

There are several ways you can access the NGRX APIs.

  * Use a Personal Access Token (PAT). For more information, go to the Platform Help from the [Help Portal](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/portal_home.htm).

  * Use a JSON Web Token (JWT), as described on this page.

## How do I use the JSON Web Token (JWT) to access NGRX APIs?

At Archer, we use JSON Web Token (JWT) to encode session information.

**Important:** While this is not required to access or use our APIs, we recommend using the JWT method for optimal performance, especially if you use automation.

Below you can find the specific steps for making the appropriate calls.

### Step 1: Obtain your token

Do one of the following:

Get an Archer Session Token using the [classic method](restfulapi/segmentsresources/authentication.htm). 

Obtain a Personal Access Token (PAT). For more information, go to the Platform Help from the [Help Portal](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/portal_home.htm).

### Step 2: Request your JWT

Your initial request must include your Archer token. In this example, replace the bolded text with your specific instance URL and token. Use either your PAT or your Archer Session Token for the **Archer Token**.

Request Example:

curl -i -X 'GET' 'https://**instance_url** /ngrx/record/v1/levels/30465' -H 'accept: application/json' -H 'cookie: __ArcherSessionCookie__=**Archer Token** '

### Step 3: Receive JWT and store for future use

From the request in Step 2, you would receive a response. Save the **JWT_value** for future use. In this example, bolded text represent information that is specific to your request.

Response Example:

HTTP/1.1 200 OK  
Content-Type: application/json; charset=utf-8  
Transfer-Encoding: chunked  
Connection: keep-alive  
Set-Cookie: **JWT_value** ; expires=**expiration** ; domain=.**instance_domain** ; path=/; secure; httponly

### Step 4: Use the JWT in future requests

To leverage the JWT, include the **JWT_value** , from the response in step 2, in all following requests. In this example, the bolded text represent information specific to your environment.

Request Example:

curl -X 'GET' '**instance_url** /ngrx/record/v1/levels/30465' -H 'accept: application/json' -H 'cookie: **JWT_value** '
