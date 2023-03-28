# d3b Arcus Manifest Prep Change History

## Release 0.1.0

# ✨ First release of Arcus Manifest Generator

Initial release builds the file manifest, participant manifest, and the participant-crosswalk manifest.

### Summary

- Emojis: 🚑️ x1, 🐛 x1, 📝 x1, 🎉 x2, 🎨 x1, ♻️ x1, ✏️ x1, ✨ x3, 🚧 x1, ? x1, 🚚 x1, 🔧 x2, 🦺 x1
- Categories: Additions x7, Documentation x1, Fixes x2, Ops x2, Other Changes x5

### New features and changes

- [#19](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/19) - 🚑️ use correct column names in file manifest - [d1fdc3d3](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/d1fdc3d303c312bfb09e876883e73b5fb663aa49) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#18](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/18) - 🐛 fix multiple bugs related to parsing mrns and with workflow - [7838c098](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/7838c09858d0f9e963d2d305f18f57be3be81149) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#17](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/17) - 📝 add documentation for undocumented functions - [4a3a20f4](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/4a3a20f4beec69d7129e2f9c30194949bb5d7932) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#10](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/10) - 🎉 Add SQL for file manifest pull - [9c3f7928](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/9c3f7928b8ce4a5619c06f242487708c09a9f340) by [youngnm](https://github.com/youngnm)
- [#15](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/15) - 🎨 Cleanup - [a3622686](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/a3622686e0cdefc339fcf7bdc9f6e2371f066bb8) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#16](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/16) - ♻️ Add option to allow unvalidated MRNs to not stop code execution - [2335fc47](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/2335fc470dd6fed096da9cac02f734e4c4834a35) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#13](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/13) - ✏️ save file manifest with correct filename - [0dc4a674](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/0dc4a67470bfd1ac3f4eb5b48dfa6214103173fb) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#14](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/14) - ✨ add participant manifest generator - [147cdee0](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/147cdee0295eaa11d01af3ca829ac6b8e6f69962) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#12](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/12) - ✨ add functionality to generate participant crosswalk - [cc9e0aa8](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/cc9e0aa8a97815a1b1bcfe0e7e91018bc859e9e0) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#9](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/9) - 🚧 add in a placeholder for qc testing - [d05bde04](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/d05bde041663df8ef66aaef6c0a35335e80075f7) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#8](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/8) - ✨ setup of tool - [ca13f7aa](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/ca13f7aa73984aa4957420670a559d967ee762ab) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#7](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/7) -  Design docs - [fa950c6e](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/fa950c6e16e985c8fff3caee331699092a931327) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#4](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/4) - 🎉 Add file-sample-participant map SQL and file - [d8495ec3](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/d8495ec371b0f53f5c1fc2c4f2aa457ca9725bc5) by [youngnm](https://github.com/youngnm)
- [#6](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/6) - 🚚 move sqlfluff to root of project so linting works - [db4f6669](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/db4f6669448134a8f1708a94451b2748c60d46f2) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#5](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/5) - 🔧 add sql linting config files - [1c65a0e0](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/1c65a0e07127b4ee038a0b29c005be7b9f7907e4) by [chris-s-friedman](https://github.com/chris-s-friedman)
- [#2](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/2) - 🦺 add validation binary and readme - [e86538b5](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/e86538b584f6df611dce44f42cfac634ad99a6ed) by [calkinsh](https://github.com/calkinsh)
- [#1](https://github.com/d3b-center/d3b-arcus-manifest-prep/pull/1) - 🔧 Repo setup - [178d89db](https://github.com/d3b-center/d3b-arcus-manifest-prep/commit/178d89db69c3058a3b301f62793ca7d633c70dbb) by [chris-s-friedman](https://github.com/chris-s-friedman)