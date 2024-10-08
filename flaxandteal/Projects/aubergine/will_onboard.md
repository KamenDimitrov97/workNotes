### Application Overview:
The application is designed for a custom office to track the movement of packages and other items through customs. It supports functionality for both incoming and outgoing packages.

### Development Status:
AUB has prototyped two of the main areas, which in total are 16. They will complete the full application.
What we are doing is:
- Ongoing support
- Knowledge transfer and training
- Ticket fixes
- Deployment support, including Docker, CI/CD, and related tools.

### Technical Details:

#### Repository & Version Control:

ASM doesn't use the same GitLab repository as fnt and galvia.
The application is moving to an Azure DevOps repository. Nothing functionally has changed, but some layouts have been updated and possibly brocken.

#### Deployment Setup:

1. Requirements:
- ASM account needed.
- Use warp-cli (available at one.one.one.one.com) instead of Cloudflare Zero Trust.
- warp-cli will connect and disconnect your network. Other internet services won’t work when connected.
Commands:
arduino
Copy code
warp-cli teams-enroll asm aeos-platform


### Themes:
FNT theme: aubergine
ASM theme: aeos


### Project Structure:
The project spans three repositories, and components shared across them should be implemented in a way that promotes reuse.
1. AEOS Platform/Website: Frontend built with Vue.js.
2. WinForm-Component-Library: Base component library with generic components such as wintextfield, wintable, etc.
3. AEOS-Component-Library: Extends the WinForm-Component-Library and customizes it for this specific application.

Previous Application:
Sequoia: The original app used by the clients before Aubergine was developed. ASM is taking over this project, and we've replicated 2-3 forms from the Sequoia app.

### Key Components:
1. aeos.component-library
2. aeos.component-library
3. winform-component-library

Example component:
- wintextfield.vue: The Vue component for input fields.
- wintextfield.ts: Defines the props interface and input-related properties.
- SCSS Variables: Stored in src/default.ts.

### Development Workflow:

### NPM Commands:

#### Storybook
!- To see how a component behaves, build the platform.
!- To initially test out component use storybook.

```sh
npm run storybook # View documentation and test component behavior.
```

### Setting up the Aubergine Version:

Use the latest version of component libraries.
To make development changes to the WinForm or library:
```sh
npm build # build the lib to use it 

# if you want to use your locally lib for testing purposes:
npm link # to link your local lib 

# Run build or if you've already have take the name from the build 
npm link build-name

# Run npm ls to verify
npm ls

# Update the version and repeat the process for the other library 
# Link both the WinForm build version and Aubergine build version in the same line :
cd aub-platform
npm link 
npm link winform-build-version aubergine-winform-build-version

# Verify 
npm ls
```

#### Unlinking:
```sh
npm install # drawback is it will change your package-lock.json
npm unlink winform-build-version aubergine-winform-build-version

# verify
npm ls
```

### Recommended vscode EXTs by Will:
- Vue Official Extensions
- Prettier for TypeScript
- GitLens
- ESLint
- YAML
- Peacock

### Tasks:

- [ ] Set up the Aubergine version while waiting for access rights.
- [ ] Having a working environment running.
- [x] Ask Phil for credentials to access ASM.