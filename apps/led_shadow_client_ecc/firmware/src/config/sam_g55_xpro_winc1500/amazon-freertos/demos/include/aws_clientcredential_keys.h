
/*
 * FreeRTOS V201906.00 Major
 * Copyright (C) 2020 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 * http://aws.amazon.com/freertos
 * http://www.FreeRTOS.org
 */

#ifndef AWS_CLIENT_CREDENTIAL_KEYS_H
#define AWS_CLIENT_CREDENTIAL_KEYS_H

/*
 * @brief PEM-encoded client certificate.
 *
 * @todo If you are running one of the FreeRTOS demo projects, set this
 * to the certificate that will be used for TLS client authentication.
 *
 * @note Must include the PEM header and footer:
 * "-----BEGIN CERTIFICATE-----
"\
 * "...base64 data...
" * "-----END CERTIFICATE-----
"
 */
#define keyCLIENT_CERTIFICATE_PEM   \
"-----BEGIN CERTIFICATE-----\n"\
"MIIBqjCCAU+gAwIBAgIQfvO0IXXZXWM+Kymy9IZUiTAKBggqhkjOPQQDAjA0MRQw\n"\
"EgYDVQQKDAtFeGFtcGxlIEluYzEcMBoGA1UEAwwTRXhhbXBsZSBTaWduZXIgRkZG\n"\
"RjAgFw0yMDEyMTUwNTAwMDBaGA8zMDAwMTIzMTIzNTk1OVowMzEUMBIGA1UECgwL\n"\
"RXhhbXBsZSBJbmMxGzAZBgNVBAMMEjAxMjNEQUU5NzRDNTVCOUFFRTBZMBMGByqG\n"\
"SM49AgEGCCqGSM49AwEHA0IABFJPTWPWHXOGmK0QhHicEuUaQ5JtBQhglB0yDbYy\n"\
"zoufzNfxPrmY7TrOqPxZ3BMozcGfkBlfxf1/Rm7gyZy1iIujQjBAMB0GA1UdDgQW\n"\
"BBTuRkACWEmTM1A3JuKNY3A1fDorsTAfBgNVHSMEGDAWgBRe4y/W9RdhRUb6mqth\n"\
"dvG49Y2e6zAKBggqhkjOPQQDAgNJADBGAiEAl7SNeBeLqB0nK3ekFE3YHYPMUuvd\n"\
"6lIyMyxWbamX2OsCIQD5Yary8ygOGqUPSPNZmN63VPWwyTizb1KjmizzhiImYw==\n"\
"-----END CERTIFICATE-----\n"\

/*
 * @brief PEM-encoded issuer certificate for AWS IoT Just In Time Registration (JITR).
 *
 * @todo If you are using AWS IoT Just in Time Registration (JITR), set this to
 * the issuer (Certificate Authority) certificate of the client certificate above.
 *
 * @note This setting is required by JITR because the issuer is used by the AWS
 * IoT gateway for routing the device's initial request. (The device client
 * certificate must always be sent as well.) For more information about JITR, see:
 *  https://docs.aws.amazon.com/iot/latest/developerguide/jit-provisioning.html,
 *  https://aws.amazon.com/blogs/iot/just-in-time-registration-of-device-certificates-on-aws-iot/.
 *
 * If you're not using JITR, set below to NULL.
 *
 * Must include the PEM header and footer:
 * "-----BEGIN CERTIFICATE-----
"\
 * "...base64 data...
" * "-----END CERTIFICATE-----
"
 */
#define keyJITR_DEVICE_CERTIFICATE_AUTHORITY_PEM  \
"-----BEGIN CERTIFICATE-----\n"\
"MIIByDCCAW6gAwIBAgIQfESyhSQBLndr1hZgt9yjPDAKBggqhkjOPQQDAjAwMRQw\n"\
"EgYDVQQKDAtFeGFtcGxlIEluYzEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMB4X\n"\
"DTIwMTIxMTA2MjIyNFoXDTMwMTIxMTA2MjIyNFowNDEUMBIGA1UECgwLRXhhbXBs\n"\
"ZSBJbmMxHDAaBgNVBAMME0V4YW1wbGUgU2lnbmVyIEZGRkYwWTATBgcqhkjOPQIB\n"\
"BggqhkjOPQMBBwNCAARCI4JfSTFEOgEaHQxEQqQE5CSHClOuJH6EgjiHvZdK6BE/\n"\
"NqCmKeKlw0k1suhRhO2FuxVXSdyqHZ3jrprzeOqxo2YwZDASBgNVHRMBAf8ECDAG\n"\
"AQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUXuMv1vUXYUVG+pqrYXbx\n"\
"uPWNnuswHwYDVR0jBBgwFoAUhQ2eVfNsdb/lmNpoYvg6y0dgHwEwCgYIKoZIzj0E\n"\
"AwIDSAAwRQIgJGsYLaVhpIMQRhHda8uJn7Yll6fox40Vg5jOmo8QpBgCIQCW7g16\n"\
"FxzI9CM8nGTSEWDm0aIxeaKPKGO/JAT1l4FKBQ==\n"\
"-----END CERTIFICATE-----\n"\

/*
 * @brief PEM-encoded client private key.
 *
 * @todo If you are running one of the FreeRTOS demo projects, set this
 * to the private key that will be used for TLS client authentication.
 *
 * @note Must include the PEM header and footer:
 * "-----BEGIN RSA PRIVATE KEY-----
"\
 * "...base64 data...
" * "-----END RSA PRIVATE KEY-----
"
 */
#define keyCLIENT_PRIVATE_KEY_PEM                   ""

#endif /* AWS_CLIENT_CREDENTIAL_KEYS_H */

