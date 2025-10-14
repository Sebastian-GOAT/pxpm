<template>

    <!-- Inputs -->
    <section class="py-8 flex justify-center">
        <div class="w-[min(550px,_100%)] flex flex-col gap-4 items-center">
            <UInput
                placeholder="Search..."
                v-model="searchQuery"
                variant="none"
                size="xl"
                class="w-full bg-bg-card border-1 border-outline rounded-md"
            />
            <UInputTags
                placeholder="Keywords..."
                v-model="keywords"
                variant="none"
                size="xl"
                :max="8"
                :max-length="20"
                class="w-full bg-bg-card border-1 border-outline"
            />
            <UButton
                class="text-white"
                size="xl"
                :href="`/search?q=${searchQuery.trim().toLowerCase()}&k=${keywords.map(k => k.trim().toLowerCase()).join(',')}`"
            >
                <Icon name="uil:search" />
                Search
            </UButton>
        </div>
    </section>

    <!-- Packages -->
    <section class="pb-8 flex justify-center">
        <div class="p-6 w-[min(550px,_100%)]">
            <h1 class="text-xl font-bold">
                Results
            </h1>
            <ul class="mt-6 flex flex-col">
                <!-- Package -->
                <li
                    v-for="(pkg, i) in packages"
                    :key="i"
                    :class="`p-4 flex justify-between items-center ${i !== packages.length - 1 ? 'border-b-1 border-b-outline' : ''}`"
                >
                    <div>
                        <h2 class="text-lg font-medium">
                            {{ pkg.name }}
                        </h2>
                        <p class="mt-2 text-muted">
                            {{ pkg.description }}
                        </p>
                    </div>
                    <UButton
                        size="lg"
                        variant="soft"
                        :href="`/package/${pkg.name}`"
                    >
                        <Icon name="uil:external-link-alt" />
                        View
                    </UButton>
                </li>
            </ul>
        </div>
    </section>

</template>

<script setup lang="ts">
definePageMeta({
    layout: 'header'
});

const route = useRoute();

const searchQuery = ref<string>((route.query.q as string) || '');
const keywords = ref<string[]>(
    typeof route.query.keywords === 'string'
        ? route.query.keywords.split(',').filter(Boolean)
        : []
);

const { data: packages } = await useFetch('/api/packages', { default: () => [] });
</script>