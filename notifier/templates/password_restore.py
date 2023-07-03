# flake8: noqa

password_restore_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Сброс пароля</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
    <!-- start hero -->
    <tr>
        <td align="center" bgcolor="#e9ecef">
            <!--[if (gte mso 9)|(IE)]>
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
                <tr>
                    <td align="center" valign="top" width="600">
            <![endif]-->
            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                <tr>
                    <td align="left" bgcolor="#ffffff"
                        style="padding: 36px 24px 0; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; border-top: 3px solid #d4dadf;">
                        <h1 style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px;">
                            Произошел сброс пароля
                        </h1>
                    </td>
                </tr>
            </table>
            <!--[if (gte mso 9)|(IE)]>
            </td>
            </tr>
            </table>
            <![endif]-->
        </td>
    </tr>
    <!-- end hero -->

    <!-- start copy block -->
    <tr>
        <td align="center" bgcolor="#e9ecef">
            <!--[if (gte mso 9)|(IE)]>
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
                <tr>
                    <td align="center" valign="top" width="600">
            <![endif]-->
            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">

                <!-- start copy -->
                <tr>
                    <td align="left" bgcolor="#ffffff"
                        style="padding: 24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                        <p style="margin: 0; margin-bottom: 16px;">
                            Здравствуйте, <span style="font-weight: bold;">{to_name}</span>!
                        </p>
                        <p style="margin: 0;">
                            Ваш новый пароль: {new_psw}
                        </p>

                    </td>
                </tr>
                <!-- end copy -->
            </table>
            <!--[if (gte mso 9)|(IE)]>
            </td>
            </tr>
            </table>
            <![endif]-->
        </td>
    </tr>
    <!-- end copy block -->

</table>
</body>
</html>
"""
