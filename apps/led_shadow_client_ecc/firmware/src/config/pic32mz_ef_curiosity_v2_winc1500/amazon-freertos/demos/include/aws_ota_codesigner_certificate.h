/*
 * FreeRTOS V202002.00
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

#ifndef __AWS_CODESIGN_KEYS__H__
#define __AWS_CODESIGN_KEYS__H__

/*
 * PEM-encoded code signer certificate
 *
 * Must include the PEM header and footer:
 * "-----BEGIN CERTIFICATE-----\n"
 * "...base64 data...\n"
 * "-----END CERTIFICATE-----\n";
 */
static const char signingcredentialSIGNING_CERTIFICATE_PEM[] = "-----BEGIN CERTIFICATE-----\n"\
"MIIBjzCCATagAwIBAgIUfYscQUFZw3G3zOepjEQAU6ubYbIwCgYIKoZIzj0EAwIw\n"\
"NTEzMDEGA1UEAwwqc2hhbm11Z2FzdW5kYXJhbS52aXN3YW5hdGhhbkBtaWNyb2No\n"\
"aXAuY29tMB4XDTIwMDUwNTExMjAxMFoXDTIxMDUwNTExMjAxMFowNTEzMDEGA1UE\n"\
"Awwqc2hhbm11Z2FzdW5kYXJhbS52aXN3YW5hdGhhbkBtaWNyb2NoaXAuY29tMFkw\n"\
"EwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEQCzIoejSThtgiRx4+vnBnnLmLk+H/KB1\n"\
"+zSDwnFk3wm2mus6iu0tOJ7G3DoXHh6Gvs5C4rAM1qbpf/UQaPuO/6MkMCIwCwYD\n"\
"VR0PBAQDAgeAMBMGA1UdJQQMMAoGCCsGAQUFBwMDMAoGCCqGSM49BAMCA0cAMEQC\n"\
"IBlcM7ME9WzeHpLgADzynqT0+bwOqxVlXTz5hSJGFcdHAiB42n5bCbEZBzWx6y21\n"\
"Jbae3R0WWtTruHdUd8ydapq/8w==\n"\
"-----END CERTIFICATE-----";
#endif
