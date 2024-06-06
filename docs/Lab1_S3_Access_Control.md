# Lab 1 - S3 Access Control

1. Create an S3 bucket named "bootcamp-s3-exercises"
    ```bash
    aws s3api create-bucket --bucket bootcamp-s3-exercises --region us-east-1
    ```

2. Create a new IAM user named "bootcamp-test-user" and generate access keys
    ```bash
    aws iam create-user --user-name bootcamp-test-user
    aws iam create-access-key --user-name bootcamp-test-user
    ```

3. Use 'aws configure' to create a profile for the bootcamp test user (e.g. --profile bootcamp-test-user) and use the access keys generated earlier

4. Use CloudShell and nano to create an IAM policy for restricted access named iam_policy.json
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "s3:ListBucket"
          ],
          "Resource": [
            "arn:aws:s3:::bootcamp-s3-exercises"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "s3:GetObject",
            "s3:DeleteObject"
          ],
          "Resource": [
            "arn:aws:s3:::bootcamp-s3-exercises/*"
          ]
        }
      ]
    }
    ```

5. Attach the IAM policy to the bootcamp-test-user
    ```bash
    aws iam put-user-policy --user-name bootcamp-test-user --policy-name BootcampTestUserPolicy --policy-document file://iam_policy.json
    ```

6. Create a bucket policy that allows the PutObject API action named bucket_policy.json
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": "arn:aws:iam::ACCOUNT_ID:user/bootcamp-test-user"
          },
          "Action": [
            "s3:PutObject"
          ],
          "Resource": [
            "arn:aws:s3:::bootcamp-s3-exercises",
            "arn:aws:s3:::bootcamp-s3-exercises/*"
          ]
        }
      ]
    }
    ```

7. Try to upload, download, and delete objects using the bootcamp-test-user profile

8. Attach the bucket policy to the bootcamp-s3-exercises bucket
    ```bash
    aws s3api put-bucket-policy --bucket bootcamp-s3-exercises --policy file://bucket_policy.json
    ```

9. Try to upload, download, and delete objects using the bootcamp-test-user profile

10. Make the object public using an object-level ACL

    Which settings must be changed?
    Does the bucket policy need updating?
    After getting it working, what happens if you enable "block public access"?

