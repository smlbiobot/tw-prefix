from twprefix import convert

VUE_SRC = """
<template>
<div class="lg:flex lg:items-center lg:justify-between">
  <div class="flex-1 min-w-0">
  </div>
</div>
</template>

<script>
export default {
  name: "Test.vue"
}
</script>

<style scoped>

</style>
"""

VUE_RESULT = """
<?xml version="1.0" encoding="utf-8"?>
<template>
  <div class="lg:tw-flex lg:tw-items-center lg:tw-justify-between">
    <div class="tw-flex-1 tw-min-w-0">
    </div>
  </div>
</template>
"""


def test_conversionI():
    dst = convert(
        VUE_SRC,
        prefix='tw-',
        indent=2,
    )
    assert dst in VUE_RESULT
