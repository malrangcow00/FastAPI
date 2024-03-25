# Status Codes

| Code | Description                                                                |
| --- |----------------------------------------------------------------------------|
|1xx| Information Response: Request Processing                                   |
|2xx| Success: Request Successfully complete                                     |
|3xx| Redirection: Further action must be taken in order to complete the request |
|4xx| Client Errors: An error was caused by the client                           |
|5xx| Server Errors: An error has occurred on the server                         |

<table>
    <th colspan="2">
        Code
    </th>
    <th>
        Description
    </th>
    <tr>
        <td colspan="2">1xx</td>
        <td colspan="2">Information Response: Request Processing</td>
    </tr>
    <tr>
        <td colspan="2">2xx</td>
        <td>Success: Request Successfully complete</td>
    </tr>
    <tr>
        <td></td>
        <td>200: OK</td>
        <td>Standard Response for a Successful Request<br>Commonly used for successful Get requests when data is being returned</td>
    </tr>
    <tr>
        <td></td>
        <td>201: Created</td>
        <td>The request has been successful, creating a new resource<br>Used when a POST creates an entity</td>
    </tr>
    <tr>
        <td></td>
        <td>204: No Content</td>
        <td>The request has been successful, did not create an entity nor return anything<br>Commonly used with PUT or DELETE request</td>
    </tr>
    <tr>
        <td colspan="2">3xx</td>
        <td>Redirection: Further action must be taken in order to complete the request</td>
    </tr>
    <tr>
        <td colspan="2">4xx</td>
        <td>Client Errors: An error was caused by the client</td>
    </tr>
    <tr>
        <td></td>
        <td>400: Bad Request</td>
        <td>Cannot process request due to client error<br>Commonly used for invalid request methods</td>
    </tr>
    <tr>
        <td></td>
        <td>401: Unauthorized</td>
        <td>Client does not have valid authentication for target resource</td>
    </tr>
    <tr>
        <td></td>
        <td>404: Not Found</td>
        <td>The clients requested resource can not be found</td>
    </tr>
    <tr>
        <td></td>
        <td>422: Unprocessable Entity</td>
        <td>Semantic Errors in Client Request</td>
    </tr>
    <tr>
        <td colspan="2">5xx</td>
        <td>Server Errors: An error has occurred on the server</td>
    </tr>
    <tr>
        <td></td>
        <td>500: Internal Server Error</td>
        <td>Generic Error Message, when an unexpected issue on the server happened</td>
    </tr>

</table>