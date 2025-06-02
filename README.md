# Resources by Urbe Bootcamp event

(this page is going to cover the notes that are from the sources provided by Urbe).

## Pre-requisites (to check in order)

Here’s a curated list of useful resouorces for participants to check before joining the Web3 bootcamp. Check and floow the links below with the provided order, as they are ordered by priority. In particular, before the bootcamp try to focus on the **mandatory** and **recommended** items.

## Typescript (mandatory)

- Typescript Crash Course – [1-hour beginner crash course](https://www.youtube.com/watch?v=BCg4U1FzODs)
- Typescript for Beginners - [Tutorials & Exercises](https://www.totaltypescript.com/tutorials/beginners-typescript)
- Solving Typescript Errors - [Tutorials & Exercises](https://www.totaltypescript.com/tutorials/solving-typescript-errors)
- Typescript Exercises - [Exercises](https://typescript-exercises.github.io/)
- Typescript Handbook - [Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

## React (mandatory)

- React Crash Course - [1.5-hour beginner crash course](https://www.youtube.com/watch?v=w7ejDZ8SWv8)
- React with Typescript - [Tutorials & Exercises](https://www.totaltypescript.com/tutorials/react-with-typescript)
- React Official Docs - [Official Docs](https://react.dev/learn)

## Next.js (recommended)

- Next.js Crash Course - [1 hour beginner crash course](https://www.youtube.com/watch?v=mTz0GXj8NN0)
- Next.js Learn - [16 chapters from React to Next.js](https://nextjs.org/learn/)
- Next.js Official Docs - [Official Docs](https://nextjs.org/docs)
- Next.js Examples - [Examples](https://github.com/vercel/next.js/tree/canary/examples)

## Blockchain (nice to have)

1. **Intro to Blockchain** - [Beginner-friendly guide by Coinbase](https://www.coinbase.com/en/learn/crypto-basics/what-is-a-blockchain)
2. Simple Blockchain explanation - [Youtube video](https://www.youtube.com/watch?v=SSo_EIwHSd4)
3. **Interactive visualization of Blockchain concepts**  - [Videos](https://andersbrownworth.com/blockchain/)
4. **Ethereum Whitepaper** - [Ethereum Whitepaper](https://ethereum.org/en/whitepaper/)
    
    Provides a comprehensive introduction to Ethereum's core concepts.
    
5. **What is the Ethereum Virtual Machine (EVM)?** - [EVM Explained](https://ethereum.org/en/developers/docs/evm/)
    
    A good overview of how the EVM works, crucial for understanding smart contract execution.
    
6. **Alchemy University Courses** - [Explore courses](https://www.alchemy.com/university/courses)
    
    Fast track your web3 journey through courses, projects and code. Totally free.
    
7. **Solidity for beginners** - [Solidity tutorial](https://cryptozombies.io/en/course)
    
    Solidity beginner to intermediate Smart Contracts
    

## Previous bootcamps recording (nice to have)

We already hosted a bunch of these bootcamps and recorded all the sessions. If you want to get up to speed, you can already start rewatching the recordings, and expect the content to be similar to what we’re going to do in Bangkok.

- **Day 1 - Intro to blockchain and EVM**: [Youtube Video](https://www.youtube.com/watch?v=fU27PVUBq74)
- **Day 2 - Hardhat and smart contracts:** [Youtube Video](https://www.youtube.com/watch?v=0suTjzhuiXI)
- **Day 3 - Testing and deploying smart contracts:** [Youtube Video](https://www.youtube.com/watch?v=It3zSYqOwU0)
- **Day 4 - Building decentralized Web Apps on the blockchain:** [Youtube Video](https://www.youtube.com/watch?v=VZpDb8I0Jvw)
- **Day 5 - Project building exercise and ideation session:** [Youtube Video](https://www.youtube.com/watch?v=z5QjXRk3yzI)

# 1 TypeScript

Video notes “TypeScript Crash Course”:

- What is TypeScript?
    - TypeScript is an open source language and is a superset of JavaScript.
    - Offers additional features to JavaScript including static types.
    - Using types is optional
    - Can be used for front-end JS as well as backend with Node.js
- Dynamic vs Static Typing.
    - In dunamically typed lanugages, the types are associated with run-time values and not named explicitly in your code.
    - In statically typed languages, you explicitly assign types to cvariables function parameters, return values, etc.
- Pros & Cons
    - PROS: More Robust, Easily Spot Bugs, Predictability, Readability…
    - Cons: Required Compilation, more complexity…
- Compiling TypeScript
    - TSC (TypeScript Compiler) is used to compiler .ts files down to JS.
    - Can watch files and report errors at compile time.
    - The tsconfig.jsom file is used to comfigure how TypeScript works.

## 🧩 Key Differences Between `interface` and `type`

| Feature | `interface` | `type` |
| --- | --- | --- |
| **Extending / Inheritance** | ✅ Supports extension via `extends` | ✅ Supports intersection via `&` |
| **Merging Definitions** | ✅ Can be declared multiple times and merged | ❌ Cannot be re-declared (error) |
| **Describing anything besides objects** | ❌ Only for object shapes | ✅ Can alias any type: primitives, unions, tuples |
| **Recommended for...** | Public APIs, class contracts | Complex type logic, unions, advanced types |
| **Runtime presence** | No (erased at compile time) | No (also erased) |
- interface can only descibe object - type alias can describe object AND everything else (e.g. primitive values such as string, number, boolean).
- type alias can easily use unility types - interface can too…

(to genarate a file structure to work with react):

```bash
npx create-react-app . --template typescript
```

This is used to create a new React app in the current directory, and set it up to use TypeScript instead of plain JavaScript.

## 🔍 `Record` vs `Map` – Key Differences

| Feature | `Record<K, V>` | `Map<K, V>` |
| --- | --- | --- |
| Type | TypeScript **type-level** utility | JavaScript **runtime** object |
| Use | Static typing for plain objects | Dynamic key-value storage |
| Key types | Usually **string** or **number** | Can be **any type**, including objects |
| Access | `obj[key]` syntax | `.get(key)` and `.set(key, value)` |
| Serialization | Easily serializable (JSON) | Not directly serializable |
| Iteration | Use `for...in` or `Object.entries()` | Use `.forEach()` or `for...of` with `.entries()` |
| Performance | Slightly faster for basic access | More features, slower for small cases |
- Use **`Record<K, V>`** when you have a fixed set of string/number keys and want **type safety**.
- Use **`Map<K, V>`** when you need **flexibility**, **object keys**, or more **dynamic behavior** at runtime.

## Using type predicates

To define a user-defined type guard, we simply need to define a funciton whose return type is a type predicate:

```tsx
function isFish(pet: Fish | Bird): pet is Fish {
	return (pet as Fish).swim !== undefined;
}
```

pet is Fish is our type predicate in this example. A predicate takes the form prarmeterName is Type, where parameterName must be the same of a parameter from the current function signature.

Any time isFish is called with some variable, TypeScript will narrow that variable to that specific type if the original type is compatiable.

```tsx
export function isAdmin(person: Person): person is Admin{
    return person.type === 'admin';
}

export function isUser(person: Person): person is User {
    return person.type === 'user';
}

export function logPerson(person: Person) {
    let additionalInformation: string = '';
    if (isAdmin(person)) {
        additionalInformation = person.role;
    }
    if (isUser(person)) {
        additionalInformation = person.occupation;
    }
    console.log(` - ${person.name}, ${person.age}, ${additionalInformation}`);
}
```

This is called a **custom type guard** that uses a **type predicate** (`person is Admin`) to tell TypeScript “If this function returns `true`, treat `person` as `Admin` from now on.”

---

<aside>
🔑

**`in` Keyword — Best for When You Don't Have a `type` Discriminator.**

</aside>

## Function Overloads

In TypeScript, we can specify a function that can be called in different ways by writing overload signatures. To do this, write some number of funciton signatures (usually two or more), fakked by the body of the funciton:

```tsx
function makeDate(timestamp: number): Date;
function makeDate(m: number, d: number, y: number): Date;
function makeDate(mOrTimestamp: number, d?: number, y?: number): Date {
  if (d !== undefined && y !== undefined) {
    return new Date(y, mOrTimestamp, d);
  } else {
    return new Date(mOrTimestamp);
  }
}
const d1 = makeDate(12345678);
const d2 = makeDate(5, 5, 5);
```

In this example, we wrote tow oeverloads: one accepting one argument, and another accepting three arguments. These first tow signatures are called the overload signatures.

## Tuple Types

A *tuple type* is another sort of Array type that knows exactly how many elements in contains, and exactly which types it contains at specific postions.

```tsx
type StringNumberPair = [string, number];
```

Here, StringNumberPair is a typle type of string and number. Like ReadonlyArray, it has not representation at runtime, but significant to TypeScript. To the type system, StringNumberPair describes arrays whose 0 index contains a string and whose 1 index contains a number.

## Generics

A majoe part of software engineering is building components that not only have well-defined and consistent APIs, but are also reusable. Components that are capable of working on the data of today as well as the data of tomorrow will give you the most flexible capabilities for builing up large software systems.

While using “any” is certainly generic in that is will cause the funciton to accept any and all types for the type of arg, we actually are losing the information about what that type was when the funciton returns. If we passed in a number, the only imfroamtion we have is that any type could be returned.

Instead, when we need a way of capturing the type of the argument in such a way that we can also use it to denote what is being returned. Here, we will use a type variable, a special kind of variable that works on types rather than values.

```tsx
function identity<Type>(arg: Type): Type {
  return arg;
}
```

When we call the funciton we can write as:

### ✅ Option 1 — **Let TypeScript infer the type**

```tsx
const result = identity("hello");
```

### ✅ Option 2 — **Explicitly specify the type**

```tsx
const result = identity<string>("hello");
```

### 🔍 What's the difference?

### 1. **Type Inference (Option 1)**

- TypeScript **automatically infers** the type of `arg` from the argument passed.
- Less typing, cleaner code.
- Most of the time, this is all you need.

**Pros:**

- Shorter and more readable.
- Leverages TypeScript's powerful inference engine.

**Cons:**

- Not helpful when the type **cannot be inferred** or is **incorrectly inferred**.

### 2. **Explicit Type Argument (Option 2)**

- You **manually specify** the generic type.
- Useful when:
    - TypeScript **can't infer correctly**.
    - You want to **override** the inferred type.
    - You want to be **explicit for clarity or documentation**.

**Pros:**

- Full control over the type.
- Useful for empty arrays, `null`, `undefined`, or union types.

**Cons:**

- Slightly more verbose.
- Can be unnecessary if inference works fine.

## Promisify the Funciton

It means to take an old-style funciton that uses a callback, and wrap it in a new funciton that returns a Promise instead.

Why is this useful?

- You do not have to nest callbacks (callback hell)
- You can use async/await instead of then() and callbacks.
- It is cleaner, especially with multiple steps.

```tsx
function promisify<T>(
  fn: (callback: (response: ApiResponse<T>) => void) => void
): () => Promise<T>
```

Then you can call as,

```tsx
const getDataPromise = promisify(getData);

const result = await getDataPromise(); // 'Hello'
```

## Modules - Introdunction

This document is divided into four sections:

1. Theory - to be able to:
    - Reason about how to integrate TypeScript with other tools.
    - Understand how TypeScript processes dependency packages.
    - Write the correct module-rekated compiler options for any situation.
2. Guides - practically know how to:
    - Pick the right compilation settings for a new project.
    - Accomplish specific real-world tasks.

### 1. Theory.

In the early days of JS, when the language only ran in browsers, there were no modules, but it was still possible to split the JavaScript for a web page into multiple files by using multiple script tags in HTML.

This approach had some downsides, especially as web pages share the same scope called the “global scope” - meaning the scripts had to be very careful not to overwirte each others’ variables and functions.

> Any system that solves this problem by giving files their own scope while still providing a way to make bits of code available to other files can be called a “module system”.
> 

There are several ways of moduling, the two most important system today: ECMAScrip modules (ESM) and CommanJS (CJS).

- ECMAScript Modules (ESM) is the module system built into the language, supported in modern browsers and in Node.js since v12. It uses dedicated import and export.

```tsx
// a.js
export default "Hello from a.js";
```

```tsx
// b.js
import a from "./a.js";
console.log(a); // 'Hello from a.js'
```

CommonJS (CJS) is the module system that originally shipped in Mode.js, before ESM was part of the language specification. It’s still supported in Node.js alongside ESM. It uses plain JavaScript objects and functions named exports and require:

```tsx
// a.js
exports.message = "Hello from a.js";
```

```tsx
// b.js
const a = require("./a");
console.log(a.message); // 'Hello from a.js'
```

There are several or more questions to ask before knowing the type of called import form another file:

- What the module system load this TypeScript file directly, or will it load a JavaScript file that I generate form this TypeScript file?
- What kind of module does the module system expect to find, given the file name it will load and its location on disk?
- If output JavaScript is being emitted, how will the module syntax present in the file be transformed in the output code?
- Where will the module system look to find the module specified by the function name?
- What find of module is the file resolved by that lookup?

Notice that all of these questions depend on characteristics of the host - the system that ultimatley consumes the output JavaScript (or raw TypeScript, as the case may be) to direct its module loading behavior, typically either a runtime (like Node.js) or bundler (like Webpack)

The other key idea to keep in mind is that TypeScript almost always thinks about these questions in terms of its output JavaScript files. So far now, we can summarize TypeScript’s job when it somes to modules in terms of output files:

Understand the rules of the host enough

1. to compile files into a valid output module format,
2. to ensure that import in those output will resolve successfully, and
3. to know what type to assign to imported names.

Who is the host?

It is a system outside of TypeScript that TypeScript’s module analysis and tries to model:

- When th output is run directly in a runtime like Node.js, the runtime is the host.
- When there is not output code because a runtime consumes TypeScript files directly

The module output format.

The module compiler option provides this information to the compiler. Its primary purpose is to control the module format of any JS that get emitted during compilation, but it also serves to inform the compiler about how the module kind of each file should be detected, how different modules kinds are called to import each other, and whether language featrues are abaiable.

Let’s look at a new example with multiple files:

```tsx
// @Filename: math.ts
export function add(a: number, b: number) {
  return a + b;
}
// @Filename: main.ts
import { add } from "./math";
add(1, 2);
```

When we see the import form “./math”, it might be tempting to think, “This is how one TypeScript file refer to another. The compiler follows this path in order to assign a type to add.”

This is not entirely wrong, but the reality is deeper. The resolution of “./math” need to reflect the reality of what happens at runtime to the output files. A more robust way to think about this process would look like this:

![theory.md-2.svg](Resources%20by%20Urbe%20Bootcamp%20event%20bba14e567c1e4de5810936e7c5833db8/theory.md-2.svg)

This model makes it clear that for TypeScript, module resolution is mostly matter of accurately modeling the host’s module resolution algorithm between output files, with a little bit of remapping applied to find type information.

The role of dearation files

In the previour example, we saw the “remapping” part of module resolution working between impute and output files. How we import library code?

This is were declaration files (.d.ts, .d.mts, etc.) come into play. The best way to understand how declaration files are interpreted is to understand where they come form.

![declaration-files.svg](Resources%20by%20Urbe%20Bootcamp%20event%20bba14e567c1e4de5810936e7c5833db8/declaration-files.svg)

In TypeScript, a **declaration file** (usually with the extension `.d.ts`) is a file that provides **type information** about JavaScript code. It tells the TypeScript compiler the **shape of the code** (functions, classes, variables, etc.) without providing the actual implementation.

They allow TypeScript to understand code written in JavaScript or in third-party libraries that may not be written in TypeScript. This enables features like **type checking**, **code completion**, and **intellisense**.

# 2. React JS Crash Course

What Is React?

- React runs on the client as a SPA(Single Page App), but can be used to build full stack apps by commuicating with a server/API.
- React is often refered to as a front-end “framework” because it is capable and directly comparable to a framework such as Angular or Vue.

Why would you use it?

- Structure the “view” layer of your application.
- Reusable components with their own state.
- Performance & testing.

What should you know first?

You should have a good handle on JavaScript. I would not suggest jumping into React without learning JavaScript first.

- Data types, variables, functions, loops, etc.
- Promises & asynchronus programming.
- Array methods like forEach() & map().
- Fetch API & making HTTP requests.

Working with State.

- Components can have “state” which is an object that determines how component renders a behaves.
- “App” or “global” state refers to state that is abailable to the entire UI, not just a single component.

## Create React App

For this purposes we can use command line promt to set up the envirnment with all boiler plate.

```bash
npx create-react-app {project-name}
```

# Day 1 - Bootcamp: Introduction to Blockchain and Ethereum.

[etherscan.io](http://etherscan.io) to know the gas price Total Cost: Transaction fee = Gas Used * Gas Price.

Ethereum functions as a single **globally accessible decentralized world** computer, allowing people to **write** and **read data** and deploy application through smart contracts.

- Decentralized: runs on thorusands of nodes worldwide, with no single enitiy in control, ensuing censorship resistance and no single point of failure.
- Turing-Complete: supports complex computations via the Ethereum Virtual Machine, enableing diverse application like DeFi and NFTs.
- Interoperable: Smart contract can interact with each other for a modular ecosystem.
- Deterministic: for the same input, the EVM always produces the same output, ensuring all nodes agree on the blochain’s state.
- Isolated: The EVM runs contracts in a sandboxed environment, preventing malicious code form accessing a node’s system or other contracts’ data directly.

EVM

- Gas is a measure of computattional effort needed for actions on Ethereum, like executing smart contract funcitons, transferring ETH, or updating blockchain state.
- Each operation in the EVM has a fixed gas cost. For example:
    - Basic transaction 21000 gas
    - Stoing a 256bit word: 20000 gas(new storage) or 5000 gas (update).
- Gas Price: Measured in gwei (1 gwei = 10 in the power of-9), this is how much ETH you are willing to pay per unit of gas. Higher gas prices prioritize faster transaction processing.
- Gas Limit: The maximum amount of gas a transcation can use, set by the sender to cap costs and prevent infinit loops.
- Total Cost: Transaction fee = Gas Used * Gas Price (in ETH)

Smart Contracts - 1

Smart contracts are programs stored on a blockchain

1. Writing: Developers write smart contracts in a language like Solidity defining rules and funciton.
2. Compilation: The code is compiled into bytecode, a format the EVM understands.
3. Deployment: The bytecode is deployed to the Ethereum blockchain via a transaction, assigning the contract a unique address.
4. Execution:
- Users interact with the contract by sending transactions to its address, calling its funciton.
- The EVM executes the code on every node, updating the blockchain’s state.
- Execution costs gas, which compenstates nodes and prevents abuse.
1. State Updates: Results are stored permaently on the blockchain, agreed upon by all nodes.

EOA Wallet

Private Key:

- A secret, 256-bit random number
- It is like a password: it proves ownership of the EOA and signs transactions to authorize actions.
- It gives you full contol over your wallet - like a master password.
- If someone has your provate key, they can spend your ETH and use your wallet.

Public Key:

- Derived form the private key using elliptic curve cryptography.
- It is sage to share with others
- It is used to create your wallet address, which other can use to send you ETH or tokens.

Smart Contracts Wallet.

Unlike EOAs, which are controlled by users via private keys, smart contracts accounts are contralled by their code and execute when called by user EOA or other contracts.

Each smart contract account has a unique address on the blockchain, similar to an EOA, but it’s associated with code and storage.

Ethereum: L1 & L2 - 1

What is it? The core Ethereum blockchain, running the EVM and securing all transactions.

Key Freatures: 

- Secure & Decentralized: Uses Proof of Stake (PoS) with thousands of nodes
- Smart Contracts: executes and stores smart contarct accouts on-chain

Challenges:

- Low throughput: 15-30 TPS
- High gas fees: $1-100 per transaction during congestion

Layer 2 (L2): Scaling Solutions

- **What is it?** Blockchains built on L1 to boost scalability and reduce costs, settling on L1 for security.
- **Key Features**
    - High Throughput: Thousands of TPS, low fees ($0.01–$1).
    - Smart Contracts: EVM-compatible, run similar contracts as L1 (cheaper gas).
- **Types**:
    - Optimistic Rollups: Assume valid transactions, challenge period (e.g., Arbitrum, Optimism).
    - ZK-Rollups: Use zero-knowledge proofs for quick validity (e.g., zkSync).

**Examples**

: Arbitrum, Optimism, zkSync.

Smart Contract development

At its core, wirting a smart contract in Solidity is not just coding logic, but about choosing the most efficient way to sore and access data in extremently constraned and costly memory eviroment.

You are not just a developer, you are a memory achitect operating under a pay-per-byte eonomy.

Smart contract development means **writing and deploying code** (usually in Solidity) that runs on a **blockchain like Ethereum**. These programs **automate actions** like transferring money, creating NFTs, or running DeFi protocols — all without needing a middleman.

# Day 2: Smart Contract development.