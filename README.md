# Tailwind Prefix

Add Tailwind Prefix to classes.

## Why?

Components found on the web using Tailwind classes are usually provided as plain Tailwind CSS classes. But very often we need to add custom prefix so that it won’t collide with existing styles. This script was written so that you can copy the source and quickly convert them into prefix’ed versions such that you can use it immediately.

## Install

Clone repo, create virutualenv (if wanted)

Install requirements

```angular2html
pip install -r requirements.txt
```

Run as module

```
python -m twprefix
```

## Example

From https://tailwindui.com/preview

```
python -m twprefix ./tests/InputGroups.vue
```

converts source:

```html
<div>
  <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
  <div class="mt-1 relative rounded-md shadow-sm">
    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
      <span class="text-gray-500 sm:text-sm">
        $
      </span>
    </div>
    <input type="text" name="price" id="price" class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md" placeholder="0.00">
    <div class="absolute inset-y-0 right-0 flex items-center">
      <label for="currency" class="sr-only">Currency</label>
      <select id="currency" name="currency" class="focus:ring-indigo-500 focus:border-indigo-500 h-full py-0 pl-2 pr-7 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md">
        <option>USD</option>
        <option>CAD</option>
        <option>EUR</option>
      </select>
    </div>
  </div>
</div>
```

to:

```html
<div>
  <label class="tw-block tw-text-sm tw-font-medium tw-text-gray-700" for="price">
    Price
  </label>
  <div class="tw-mt-1 tw-relative tw-rounded-md tw-shadow-sm">
    <div class="tw-absolute tw-inset-y-0 tw-left-0 tw-pl-3 tw-flex tw-items-center tw-pointer-events-none">
      <span class="tw-text-gray-500 sm:tw-text-sm">
        $
      </span>
    </div>
    <input class="focus:tw-ring-indigo-500 focus:tw-border-indigo-500 tw-block tw-w-full tw-pl-7 tw-pr-12 sm:tw-text-sm tw-border-gray-300 tw-rounded-md" id="price" name="price" placeholder="0.00" type="text">
      <div class="tw-absolute tw-inset-y-0 tw-right-0 tw-flex tw-items-center">
        <label class="tw-sr-only" for="currency">
          Currency
        </label>
        <select class="focus:tw-ring-indigo-500 focus:tw-border-indigo-500 tw-h-full tw-py-0 tw-pl-2 tw-pr-7 tw-border-transparent tw-bg-transparent tw-text-gray-500 sm:tw-text-sm tw-rounded-md" id="currency" name="currency">
          <option>
            USD
          </option>
          <option>
            CAD
          </option>
          <option>
            EUR
          </option>
        </select>
      </div>
    </input>
  </div>
</div>
```

## To-Do

- Add direct output
- Overwrite option
- Prevent prefixed classes from being prefixed again
