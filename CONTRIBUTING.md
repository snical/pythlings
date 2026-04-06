# Contributing to pythlings

Thanks for taking the time to help with `pythlings`.

The goal is a clean learning curve from easy to hard, without hiding what learners actually need to do.

When you add or edit an exercise, keep these in sync:

1. `exercises/...`
2. `solutions/...`
3. `.pythlings/starters/...`
4. `.pythlings/validators/...` when that exercise uses validator-based checking

- Keep early exercises small and obvious.
- Keep the order easy to hard, both within a category and across categories.
- Keep hints helpful without giving away the answer.
- Use validators when output comparison is not enough.
- Make validator failures clear enough that learners can tell what went wrong.

Before opening a PR:

- run the CLI and confirm it still finds the first broken exercise correctly
- make sure edited exercises are actually broken in `exercises/`
- make sure the matching `solutions/` file passes
- make sure reset still restores from `.pythlings/starters/`
- check that the order still makes sense
