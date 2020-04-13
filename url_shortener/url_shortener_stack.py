from aws_cdk import core, aws_dynamodb


class UrlShortenerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        '''The below line, with only one line of code, will create a DynamoDB table that is name "url-shortener-table" 
        as well as having one defined attribute of type String call "id"
        '''
        table = aws_dynamodb.Table(self, "url-shortner-table",
                                   partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING))