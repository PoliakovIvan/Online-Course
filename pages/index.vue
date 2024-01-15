<script setup>
const data = {
    "courses": [
        {
            "image": "/images/main/mentor-2.jpg",
            "category": "Marketing",
            "name": "The ultimate google ads training course",
            "price": "100",
            "mentor": "Ryan Thomas Gosling"
        },
        {
            "image": "/images/main/mentor-1.jpg",
            "category": "Management",
            "name": "Business Development Management",
            "price": "400",
            "mentor": "Dianne Russell"
        },
        {
            "image": "/images/main/mentor-1.jpg",
            "category": "Management",
            "name": "Business Development Management",
            "price": "400",
            "mentor": "Dianne Russell"
        },
        {
            "image": "/images/main/mentor-2.jpg",
            "category": "Marketing",
            "name": "The ultimate google ads training course",
            "price": "100",
            "mentor": "Ryan Thomas Gosling"
        }
    ],
    "mentors": [
        {
            "image": "/images/main/mentor-2.jpg",
            "name": "Ryan Thomas Gosling",
            "position": "Founder and Program Director"
        },
        {
            "image": "/images/main/mentor-1.jpg",
            "name": "Dianne Russell",
            "position": "Founder and CEO"
        },
        {
            "image": "/images/main/mentor-2.jpg",
            "name": "Ryan Thomas Gosling",
            "position": "Founder and Program Director"
        },
        {
            "image": "/images/main/mentor-1.jpg",
            "name": "Dianne Russell",
            "position": "Founder and CEO"
        }
    ]
}
</script>

<template>
    <NuxtLayout name="main">
        <div class="container">
            <main-section heading="Featured Courses" subtitle="Ready to learn?">
                <div class="grid grid-cols-2">
                    <course-card-v v-for="item in data.courses" :key="JSON.stringify(item)" :itemData="item" />
                </div>
            </main-section>
            <main-section heading="Meet our team" subtitle="Best tutors are all here">
                <div class="grid grid-cols-4">
                    <mentor-card v-for="item in data.mentors" :key="JSON.stringify(item)" :itemData="item" />
                </div>
            </main-section>
        </div>
    </NuxtLayout>
</template>