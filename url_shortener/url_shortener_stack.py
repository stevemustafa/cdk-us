from aws_cdk import core, aws_dynamodb, aws_lambda, aws_apigateway


class UrlShortenerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        '''
        v0.1
        The below line, with only one line of code, will create a DynamoDB table that is name "url-shortener-table" 
        as well as having one defined attribute of type String call "id"
        '''
        table = aws_dynamodb.Table(self, "url-shortner-table",
                                   partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING))

        '''
        v0.2
        As we did previously with creating DynamoDB, we now create a Lambda function.
        Please take note of the following:
        * the "runtime" is defined from the static class aws_lambda.Runtime.<Runtime>
        * the handler is referencing the function "main" in the handler.py file
        * Code refers to the bundling of code assets from the entire directory ./lambda
        '''

        function = aws_lambda.Function(self, 'backend',
                                       runtime=aws_lambda.Runtime.PYTHON_3_7,
                                       handler='handler.main',
                                       code=aws_lambda.Code.asset('./lambda'))

        '''
        v0.3 
        The following creates the tie in between the lambda function and the dynamodb table by granting read and write 
        permissions to the function on the table itself
        this also involves injecting environment variables - please refer to the file handler.py to see where the 
        environment variable is used
        '''
        # create the tie in between the lambda function and the DynamoDB table
        table.grant_read_write_data(function)

        # add the environment variable for the function to consume
        function.add_environment("TABLE_NAME", table.table_name)