Claris also published an [official Database Design Report (DDR) XML output grammar](https://help.claris.com/archive/docs/17/en/ddrxml/), including a Script Section that documents how scripts and each script step are represented in DDR XML. It even shows per-step XML structures and explains quirks like saved secondary options showing up even when not active.

Important reality check:
* DDR XML is not the same as clipboard fmxmlsnippet, but it’s close enough to be extremely valuable:
* Step IDs and step names are consistent anchors.
* Many sub-elements correspond conceptually (parameters, calculations, targets).
* DDR provides documented XML grammar you can cross-check against your reverse-engineered clipboard format.

There is no official spec for <fmxmlsnippet>, but this is the nearest thing Claris has ever shipped.

The [steps-documentation-for-ddr.html]() file contains a copy of the relevant bit for Claris' documentation. They also provide the following note:
    Many script steps have options or attributes that are determined by their associated secondary options. If you change a secondary option, FileMaker Pro Advanced retains its last-used settings and stores them with the script step. If you later revert your choice, those settings will be available again.

    For example, when you select Specify find requests for the Perform Find script step and choose settings in the Specify Find Requests dialog box, those settings are saved with the script step. If you later deselect Specify find requests, FileMaker Pro Advanced doesn't use the settings when it runs the script. However, if you again select the checkbox, those saved settings will be used for the script step.

    When you generate a DDR, saved settings for secondary options appear in the report even if they're not currently being used for the script step. To determine whether the options are in effect, you must check the reported XML setting.

    The script steps shown below contain the element <StepText>, and many script steps contain instances of the element <DisplayCalculation>. Both elements contain redundant information in order to make DDR reports (in particular, HTML reports) more readable.
