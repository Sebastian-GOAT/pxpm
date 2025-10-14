<template>

    <!-- Inputs -->
    <section>
        <UInput
            placeholder="Search..."
        />
        <UInputTags
            placeholder="Keywords..."
        />
        <UButton></UButton>
    </section>

    <!-- Packages -->
    <section>

    </section>

</template>

<script setup lang="ts">

definePageMeta({
    layout: 'header'
});

useHead({
    title: 'Home | pxpm'
});

const keywordsRef = ref('');

</script>