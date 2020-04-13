import setuptools


with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="url shortener",
    version="0.0.1",

    description="A demo URL shortener application based on Lambda, DynamoDB and is built with CDK",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Steven Mustafa",

    package_dir={"": "url_shortener"},
    packages=setuptools.find_packages(where="url_shortener"),

    install_requires=[
        "aws-cdk.core==1.32.1",
        "aws-cdk.aws-dynamodb",
        "aws-cdk.aws-events",
        "aws-cdk.aws-events-targets",
        "aws-cdk.aws-lambda",
        "aws-cdk.aws-s3",
        "aws-cdk.aws-ec2",
        "aws-cdk.aws-ecs-patterns",
        "aws-cdk.aws-certificatemanager",
        "aws-cdk.aws-apigateway",
        "aws-cdk.aws-cloudwatch",
        "Cdk-watchful",
        "boto3"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)

