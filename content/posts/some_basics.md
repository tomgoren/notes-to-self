+++
title = 'Basic intro to computer stuff'
date = 2018-07-06
+++

## Objective
In this article, you will learn some basic concepts and key terms related to
computers. It will serve to prepare you for future articles in which you will
learn actual practical things.

## Who is this for?
This guide is for the absolute beginner. It assumes only that you have a computer,
know how to read, and are willing to experiment a bit with something new and
possibly very foreign.

## Key terms

### Computer

```
            Computer
          |----------|
Input --> | Do stuff | --> Output
          |----------|
```

There are many different types of computers. Some are highly specific, for
instance, devices used to control electronic systems in cars. Others are
more multifunctional, like a laptop or a smartphone. These can serve a wide range
of purposes, from writing dissertations, through reading the news, to sharing
pictures of food on social media.

### Server
A `server` is a type of computer that users (you and I), don't usually interact
with directly. `A server is a type of computer that other computers communicate
with`. It does not have a keyboard or a screen attached to it, and it usually
resides in an air conditioned room, in a special building called a Data Center.
These computers do not look like laptop or desktop computers, as they are not
designed to sit on a lap or a desk. They are "rack mounted", that is, they are
designed to be mounted in racks, which are metal cabinets designed solely for the
purpose of hosting these machines.

Here are some servers in a data center:

![Servers in a data center](/images/proper_servers_resized.jpg)

_I was part of the team that installed these servers in 2015._

When on a budget, servers might look like this:

![Deconstructed post modern server](/images/improper_server_resized.jpg)

_This was a server put together in a hurry, as part of a side project in 2007._

### Hardware
`Hardware` refers to physical objects. These objects are the parts we interact
with, like keyboards and screens, and also the electronic bits and pieces inside
of devices, like microprocessors and memory chips. The details about these elements
are outside the scope of this article (and not important right now).

Examples of hardware:

* A laptop
* A mouse
* A thumb drive
* A smartphone
* A server

### Software
Computers work by following instructions. These sets of instructions are called
`programs`. Programs are written in special languages called "programming languages".
There are many different programming languages, and they can seem very different
from each other, though for the most part, they work very similarly behind the scenes.

Much like conventional human languages, like Chinese or Amharic, programming languages
can differ in style and syntax, and much like our languages, they can be used to
convey the same ideas. "Pass the salt please" would be expressed very differently in Arabic
and in Norwegian, but they both mean the same thing and will hopefully achieve the
same result.

Below are two snippets of code. **Don't be alarmed!** There is no need to be concerned
with the details of these examples just yet, they are here only for illustrative purposes.
`C` and `Python` are examples of popular programming languages.

#### "Hello World!" in Python

```python
#!/usr/bin/env python

print("Hello, World!")
```

#### "Hello World!" in C

```c
#include <stdio.h>

int main()
{
   printf("Hello, World!\n");
   return 0;
}
```

Even though these two `programs` look very different, they will do the same thing,
namely, print out the phrase "Hello, World!" when run.

Programming languages use words from English and assign special meaning to them.

e.g.:

* `function`
* `for`
* `while`

In addition, punctuation marks and braces are utilized extensively.

e.g.:

* `!`
* `'`
* `()`
* `{}`
* `[]`

Finally, characters that are fairly unique to programming, that are not typically used
in human languages, are employed, such as:

* `|`
* `*`
* `^`

A couple of examples of these special characters that have made their way into
our everyday vernacular in an odd feat of digital culture are the "at" sign, or
`@`, and the "hashtag", `#`, also known as the pound sign.

The text of the programs we write is called `code`. There is much more to say
about software, however, this will suffice for now.

### Operating System
As you just learned, computers do things based on instructions (software) given
to them by humans. The `Operating System` is a fundamental piece of software
that enables us (developers, operators, users) to make use of the computer.
Without an operating system, or OS for short, a computer is just a hunk of
plastic and metal.

Examples of operating systems include:

* Android
* iOS
* OS X
* Windows
* Linux

The OS I care about the most, and will focus the vast majority of my writing about,
is Linux. I will go into detail about this choice and its meaning later on. For
now, I will only add that there are practical, as well as ethical and political
reasons for this.

### Special mention: Firmware
It is important to mention a special kind of software, known as `firmware`.
Firmware is a kind of code that is built-in, or `embedded`, into the hardware.
There is no need at this point to know much about it, other than that it exists.

## Conclusion
The key terms covered here were:

* `Computer` - gets input, does stuff, produces output
* `Server` - a computer that talks to other computers, not so much to humans
* `Hardware` - physical devices
* `Software` - code we write to tell computers what to do
* `Operating System` - essential software without which we cannot use the hardware
* `Firmware` - special software that we do not typically interact with at all
