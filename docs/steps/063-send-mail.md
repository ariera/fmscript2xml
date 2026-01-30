---
id: 63
name: "Send Mail"
category: Miscellaneous
status: draft
input_patterns:
  - "Send Mail [ ... ]"
fm_name: "Send Mail"
xml:
  step_name: "Send Mail"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Send Mail

## Mapping rules

- `name="Send Mail"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="63"` for all `Send Mail` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="63" name="Send Mail">
            <NoInteract state="True"/>
            <Attachment>
               <UniversalPathList>...</UniversalPathList>
            </Attachment>
   <To UseFoundSet="True">
               <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
            </To>
   <Cc UseFoundSet="True">
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </Cc>
   <Bcc UseFoundSet="True">
               <Calculation>
                 <![CDATA[<Step enable="True" id="63" name="Send Mail">
               </Calculation>
            </Bcc>
   <Subject>
               <Calculation>
                 <![CDATA["Subject"]]>
              </Calculation>
            </Subject>
   <Message>
               <Calculation>
                 <![CDATA["Message"]]>
               </Calculation>
            </Message>
  <SMTPNameDescription>
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPNameDescription>
   <SMTPEmailAddress >
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPEmailAddress>
   <SMTPReplyAddress >
              <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
           </SMTPReplyAddress>
   <SMTPServer>
              <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPServer>
   <SMTPPort >
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPPort>
   <SMTPUserName>
                <Calculation>
                  <![CDATA[CalcString]]>
               </Calculation>
            </SMTPUserName>
   <SMTPPassword >
               <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
            </SMTPPassword>
   <MultipleEmails state="True"/>
            <SendViaSMTP state ="True"/>
            <SMTPEncryptionType type="encryptionVal">
            <SMTPAuthenticationType type = "SMTPAuthenticationPlain"/>
          </Step>
```
