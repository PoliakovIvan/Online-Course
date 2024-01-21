<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation } from 'swiper/modules';
import 'swiper/scss';
import 'swiper/scss/navigation';

const modules = [Navigation];
const data = {
    "courses": [
        {
            "image": "/images/main/mentor-2.webp",
            "category": "Marketing",
            "name": "The ultimate google ads training course",
            "price": "100",
            "mentor": "Ryan Thomas Gosling"
        },
        {
            "image": "/images/main/mentor-1.webp",
            "category": "Management",
            "name": "Business Development Management",
            "price": "400",
            "mentor": "Dianne Russell"
        },
        {
            "image": "/images/main/mentor-4.webp",
            "category": "Management",
            "name": "Prduct Management Fundamentals",
            "price": "480",
            "mentor": "Marvin McKinney"
        },
        {
            "image": "/images/main/mentor-3.webp",
            "category": "Marketing",
            "name": "Brand Management & PR Communications",
            "price": "530",
            "mentor": "Kristin Watson"
        }
    ],
    "mentors": [
        {
            "image": "/images/main/mentor-2.webp",
            "name": "Ryan Thomas Gosling",
            "position": "Founder and Program Director"
        },
        {
            "image": "/images/main/mentor-1.webp",
            "name": "Dianne Russell",
            "position": "Founder and CEO"
        },
        {
            "image": "/images/main/mentor-3.webp",
            "name": "Kristin Watson",
            "position": "Marketer, Curator of Marketing Course"
        },
        {
            "image": "/images/main/mentor-4.webp",
            "name": "Marvin McKinney",
            "position": "PM, Curator of Management Course"
        },
        {
            "image": "/images/main/mentor-5.webp",
            "name": "Kathryn Murphy",
            "position": "HR manager"
        },
        {
            "image": "/images/main/mentor-6.webp",
            "name": "Cody Fisher",
            "position": "Team lead, Front-end developer"
        }
    ]
}
</script>

<template>
    <NuxtLayout name="main">
        <div class="container">
            <main-section>
                <template v-slot:heading>
                    <section-heading title="Featured Courses" subtitle="Ready to learn?" />
                    <outline-button url="#" />
                </template>
                <template v-slot:content>
                    <div class="grid grid-cols-2">
                        <course-card-v v-for="item in data.courses" :key="JSON.stringify(item)" :itemData="item" />
                    </div>
                </template>
            </main-section>
            <main-section>
                <template v-slot:heading>
                    <section-heading title="Meet our team" subtitle="Best tutors are all here" />
                    <div class="pare-button">
                        <radius-button />
                        <radius-button class="next" />
                    </div>
                </template>
                <template v-slot:content>
                    <swiper :space-between="32" :slides-per-view="4" :navigation="true" :modules="modules">
                        <swiper-slide v-for="item in data.mentors" :key="JSON.stringify(item)">
                            <mentor-card :itemData="item" />
                        </swiper-slide>
                    </swiper>
                </template>
            </main-section>
        </div>
    </NuxtLayout>
</template>