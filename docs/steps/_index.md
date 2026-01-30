---
title: "FileMaker Script Steps Catalog"
description: "Index of FileMaker script steps supported by the txt2xml agent."
version: 0.2
---

## Purpose

This folder contains **one file per FileMaker script step**, documenting:

- The step id and name.
- Accepted plain-text input patterns.
- Mapping rules to XML.
- Examples and edge cases.

Each file starts with a small YAML header, followed by markdown documentation.

## Files

### Account (6 steps)

- `083-change-password.md` — `Change Password` script step.
- `134-add-account.md` — `Add Account` script step.
- `135-delete-account.md` — `Delete Account` script step.
- `136-reset-account-password.md` — `Reset Account Password` script step.
- `137-enable-account.md` — `Enable Account` script step.
- `138-re-login.md` — `Re-Login` script step.

### Control (21 steps)

- `001-perform-script.md` — `Perform Script` script step.
- `062-pauseresume-script.md` — `Pause/Resume Script` script step.
- `068-if.md` — `If` script step.
- `069-else.md` — `Else` script step.
- `070-end-if.md` — `End If` script step.
- `071-loop.md` — `Loop` script step.
- `072-exit-loop-if.md` — `Exit Loop If` script step.
- `073-end-loop.md` — `End Loop` script step.
- `084-set-layout-object-animation.md` — `Set Layout Object Animation` script step.
- `085-allow-user-abort.md` — `Allow User Abort` script step.
- `086-set-error-capture.md` — `Set Error Capture` script step.
- `090-halt-script.md` — `Halt Script` script step.
- `103-exit-script.md` — `Exit Script` script step.
- `125-else-if.md` — `Else If` script step.
- `141-set-variable.md` — `Set Variable` script step.
- `145-go-to-object.md` — `Go to Object` script step.
- `146-set-web-viewer.md` — `Set Web Viewer` script step.
- `148-install-ontimer-script.md` — `Install OnTimer Script` script step.
- `164-perform-script-on-server.md` — `Perform Script on Server` script step.
- `185-configure-region-monitor-script.md` — `Configure Region Monitor Script` script step (vnewto16).
- `187-configure-local-notification.md` — `Configure Local Notification` script step (vnewto17).

### Editing (8 steps)

- `045-undoredo.md` — `Undo/Redo` script step.
- `046-cut.md` — `Cut` script step.
- `047-copy.md` — `Copy` script step.
- `048-paste.md` — `Paste` script step.
- `049-clear.md` — `Clear` script step.
- `050-select-all.md` — `Select All` script step.
- `128-perform-findreplace.md` — `Perform Find/Replace` script step.
- `130-set-selection.md` — `Set Selection` script step.

### Fields (21 steps)

- `011-insert-from-index.md` — `Insert from Index` script step.
- `012-insert-from-last-visited.md` — `Insert from Last Visited` script step.
- `013-insert-current-date.md` — `Insert Current Date` script step.
- `014-insert-current-time.md` — `Insert Current Time` script step.
- `040-relookup-field-contents.md` — `Relookup Field Contents` script step.
- `056-insert-picture.md` — `Insert Picture` script step.
- `060-insert-current-user-name.md` — `Insert Current User Name` script step.
- `061-insert-text.md` — `Insert Text` script step.
- `076-set-field.md` — `Set Field` script step.
- `077-insert-calculated-result.md` — `Insert Calculated Result` script step.
- `078-obsoleteinsert-object.md` — `#[OBSOLETE]Insert Object` script step.
- `091-replace-field-contents.md` — `Replace Field Contents` script step.
- `096-obsoleteupdate-link.md` — `#[OBSOLETE]Update Link` script step.
- `116-set-next-serial-value.md` — `Set Next Serial Value` script step.
- `131-insert-file.md` — `Insert File` script step.
- `132-export-field-contents.md` — `Export Field Contents` script step.
- `147-set-field-by-name.md` — `Set Field By Name` script step.
- `158-insert-pdf.md` — `Insert PDF` script step.
- `159-insert-audiovideo.md` — `Insert Audio/Video` script step.
- `160-insert-from-url.md` — `Insert from URL` script step.
- `161-insert-from-device.md` — `Insert from Device` script step.

### Files (8 steps)

- `033-open-file.md` — `Open File` script step.
- `034-close-file.md` — `Close File` script step.
- `037-save-a-copy-as.md` — `Save a Copy as` script step.
- `082-new-file.md` — `New File` script step.
- `084-set-multi-user.md` — `Set Multi-User` script step.
- `094-set-use-system-formats.md` — `Set Use System Formats` script step.
- `095-recover-file.md` — `Recover File` script step.
- `139-convert-file.md` — `Convert File` script step.

### Found Sets (13 steps)

- `021-unsort-records.md` — `Unsort Records` script step.
- `023-show-all-records.md` — `Show All Records` script step.
- `024-modify-last-find.md` — `Modify Last Find` script step.
- `025-omit-record.md` — `Omit Record` script step.
- `026-omit-multiple-records.md` — `Omit Multiple Records` script step.
- `027-show-omitted-only.md` — `Show Omitted Only` script step.
- `028-perform-find.md` — `Perform Find` script step.
- `039-sort-records.md` — `Sort Records` script step.
- `126-constrain-found-set.md` — `Constrain Found Set` script step.
- `127-extend-found-set.md` — `Extend Found Set` script step.
- `150-perform-quick-find.md` — `Perform Quick Find` script step.
- `154-sort-records-by-field.md` — `Sort Records by Field` script step.
- `155-find-matching-records.md` — `Find Matching Records` script step.

### Miscellaneous (21 steps)

- `044-exit-application.md` — `Exit Application` script step.
- `057-send-event.md` — `Send event` script step.
- `063-send-mail.md` — `Send Mail` script step.
- `064-send-dde-execute.md` — `Send DDE Execute` script step.
- `065-dial-phone.md` — `Dial Phone` script step.
- `066-speak.md` — `Speak` script step.
- `067-perform-applescript.md` — `Perform AppleScript` script step.
- `087-show-custom-dialog.md` — `Show Custom Dialog` script step.
- `089-comment.md` — `Comment` script step.
- `093-beep.md` — `Beep` script step.
- `102-flush-cache-to-disk.md` — `Flush Cache to Disk` script step.
- `111-open-url.md` — `Open URL` script step.
- `115-allow-toolbars.md` — `Allow Toolbars` script step.
- `117-execute-sql.md` — `Execute SQL` script step.
- `142-install-menu-set.md` — `Install Menu Set` script step.
- `167-refresh-object.md` — `Refresh Object` script step.
- `173-get-directory.md` — `Get Directory` script step.
- `177-avplayer-play.md` — `AVPlayer Play` script step.
- `178-avplayer-set-playback-state.md` — `AVPlayer Set Playback State` script step.
- `179-avplayer-set-options.md` — `AVPlayer Set Options` script step.
- `180-refresh-portal.md` — `Refresh Portal` script step.

### Navigation (11 steps)

- `004-go-to-next-field.md` — `Go to Next Field` script step.
- `005-go-to-previous-field.md` — `Go to Previous Field` script step.
- `006-go-to-layout.md` — `Go to Layout` script step.
- `016-go-to-recordrequestpage.md` — `Go to Record/Request/Page` script step.
- `017-go-to-field.md` — `Go to Field` script step.
- `022-enter-find-mode.md` — `Enter Find Mode` script step.
- `041-enter-preview-mode.md` — `Enter Preview Mode` script step.
- `055-enter-browse-mode.md` — `Enter Browse Mode` script step.
- `074-go-to-related-record.md` — `Go to Related Record` script step.
- `099-go-to-portal-row.md` — `Go to Portal Row` script step.
- `169-close-popover.md` — `Close Popover` script step.

### Open Menu Item (16 steps)

- `032-open-help.md` — `Open Help` script step.
- `038-open-manage-database.md` — `Open Manage Database` script step.
- `088-open-script-workspace.md` — `Open Script Workspace` script step.
- `105-open-preferences.md` — `Open Preferences` script step.
- `112-open-manage-value-lists.md` — `Open Manage Value Lists` script step.
- `113-open-sharing.md` — `Open Sharing` script step.
- `114-open-file-options.md` — `Open File Options` script step.
- `118-span-class.md` — `<span class=` script step.
- `129-open-findreplace.md` — `Open Find/Replace` script step.
- `140-open-manage-data-sources.md` — `Open Manage Data Sources` script step.
- `149-open-edit-saved-finds.md` — `Open Edit Saved Finds` script step.
- `151-open-manage-layouts-.md` — `Open Manage Layouts ` script step.
- `156-open-manage-containers.md` — `Open Manage Containers` script step.
- `165-open-manage-themes.md` — `Open Manage Themes` script step.
- `172-upload-to-filemaker-server.md` — `Upload to FileMaker Server` script step.
- `183-span-class.md` — `<span class=` script step (vnewto16).

### Records (16 steps)

- `007-new-recordrequest.md` — `New Record/Request` script step.
- `008-duplicate-recordrequest.md` — `Duplicate Record/Request` script step.
- `009-delete-recordrequest.md` — `Delete Record/Request` script step.
- `010-delete-all-records.md` — `Delete All Records` script step.
- `035-import-records.md` — `Import Records` script step.
- `036-export-records.md` — `Export Records` script step.
- `051-revert-recordrequest.md` — `Revert Record/Request` script step.
- `075-commit-recordsrequests.md` — `Commit Records/Requests` script step.
- `098-copy-all-recordsrequests.md` — `Copy All Records/Requests` script step.
- `101-copy-recordrequest.md` — `Copy Record/Request` script step.
- `104-delete-portal-row.md` — `Delete Portal Row` script step.
- `133-open-recordrequest.md` — `Open Record/Request` script step.
- `143-save-records-as-excel.md` — `Save Records as Excel` script step.
- `144-save-records-as-pdf.md` — `Save Records as PDF` script step.
- `152-save-records-as-snapshot-link.md` — `Save Records as Snapshot Link` script step.
- `182-truncate-table.md` — `Truncate Table` script step (vnewto15).

### Sort/Find/Print (2 steps)

- `042-print-setup.md` — `Print Setup` script step.
- `043-print.md` — `Print` script step.

### Spelling (7 steps)

- `018-check-selection.md` — `Check Selection` script step.
- `019-check-record.md` — `Check Record` script step.
- `020-check-found-set.md` — `Check Found Set` script step.
- `106-correct-word.md` — `Correct Word` script step.
- `107-spelling-options.md` — `Spelling Options` script step.
- `108-select-dictionaries.md` — `Select Dictionaries` script step.
- `109-edit-user-dictionary.md` — `Edit User Dictionary` script step.

### Windows (16 steps)

- `029-showhide-toolbars.md` — `Show/Hide Toolbars` script step.
- `030-view-as.md` — `View As` script step.
- `031-adjust-window.md` — `Adjust Window` script step.
- `079-freeze-window.md` — `Freeze Window` script step.
- `080-refresh-window.md` — `Refresh Window` script step.
- `081-scroll-window.md` — `Scroll Window` script step.
- `092-showhide-text-ruler.md` — `Show/Hide Text Ruler` script step.
- `097-set-zoom-level.md` — `Set Zoom Level` script step.
- `119-moveresize-window.md` — `Move/Resize Window` script step.
- `120-arrange-all-windows.md` — `Arrange All Windows` script step.
- `121-close-window.md` — `Close Window` script step.
- `122-new-window.md` — `New Window` script step.
- `123-select-window.md` — `Select Window` script step.
- `124-set-window-title.md` — `Set Window Title` script step.
- `166-showhide-menubar.md` — `Show/Hide Menubar` script step.
- `174-enable-touch-keyboard.md` — `Enable Touch Keyboard` script step.

As you add more steps, list them here for quick reference.
