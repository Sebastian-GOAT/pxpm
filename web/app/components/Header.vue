<template>
    <header class="px-8 h-16 flex justify-between items-center border-b-1 border-b-outline">

        <!-- Logo -->
        <NuxtLink href="/" class="text-xl font-semibold flex items-center gap-2">
            <Icon name="simple-icons:nuxt" :size="30" class="text-primary" />
            PXPM
        </NuxtLink>

        <!-- Navigation -->
        <nav>
            <ul class="flex items-center gap-16">
                <li v-for="link in links" :key="link.title">
                    <NuxtLink :href="link.href" class="flex items-center gap-2 text-white/60" active-class="text-white/100">
                        <Icon :name="link.icon" :size="20" />
                        {{ link.title }}
                    </NuxtLink>
                </li>
            </ul>
        </nav>

        <!-- Profile / Login -->
        <NuxtLink
            v-if="auth"
            href="/account"
            class="aspect-square w-10 border-1 border-white/20 rounded-full"
        >
            
        </NuxtLink>
        <div v-else class="flex items-center gap-4">
            <UButton
                color="neutral"
                size="lg"
                href="/auth/signup"
            >
                Sign up
            </UButton>
            <UButton
                variant="subtle"
                color="neutral"
                size="lg"
                href="/auth/login"
            >
                Log in
            </UButton>
        </div>

    </header>
</template>

<script setup lang="ts">

const auth = ref(null);

interface Link {
    title: string;
    icon: string;
    href: string;
}

const links: Link[] = [
    { title: 'Home', icon: 'uil:home-alt', href: '/' },
    { title: 'Explore', icon: 'uil:search', href: '/search' },
    { title: 'Docs', icon: 'uil:book-alt', href: '/docs' },
    { title: 'About', icon: 'uil:question-circle', href: '/about' }
];

</script>