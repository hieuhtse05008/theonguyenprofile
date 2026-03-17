import os
import requests
import json

def download_image(url, path):
    # Try one more time if it fails or if it's already there (to ensure fresh version)
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f:
                for chunk in response:
                    f.write(chunk)
            print(f"Downloaded: {path}")
        else:
            print(f"Failed to download {url}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

projects_assets = {
    1: [
        "http://localhost:3845/assets/ed5f8c7a7440786b90802de157c3f5b622dfa19e.png",
        "http://localhost:3845/assets/0e60f356fc1cd3f89501acd9e1b91a31fd0388bb.png",
        "http://localhost:3845/assets/11442554a0f826176092200f97512293d0d2b9a9.png",
        "http://localhost:3845/assets/cb3ade7514c2fc2b51cf446b050880d9654a418e.png",
        "http://localhost:3845/assets/e13c1b335cd6fc8bd1ce87e61fb57ae164e185fe.png",
        "http://localhost:3845/assets/15899b778c52cb20b36c6fad850b9e63eb455699.png",
        "http://localhost:3845/assets/12abbed28d848b9773883f9ce09c11876f3ca62e.png",
        "http://localhost:3845/assets/fcf9c06023360848ea2556439994afaccce97849.png",
        "http://localhost:3845/assets/92f82dd98e6b9225e755ac708132a1859e82841f.png",
        "http://localhost:3845/assets/4fde08d7a2621b7c9f85b9b0a1a55cf4ee8587e3.png",
        "http://localhost:3845/assets/24656cf67aabe569fb9b37ea7996614752df18cd.png",
        "http://localhost:3845/assets/dd5417650f754bf16191bf2ef4a0a5e026570c35.png",
        "http://localhost:3845/assets/9cd16cea99dfcda4748ec168ccc7571623ec258f.png",
        "http://localhost:3845/assets/848f51457534b2a6c360807e785f1ab0042a7bcf.png",
        "http://localhost:3845/assets/300fa6cc4b814efd914ab25f13b445f0a77cb040.png",
        "http://localhost:3845/assets/10d996b3e29345e7e45d80198a02b5f12956a1a5.png",
        "http://localhost:3845/assets/bbbd02df87d7fd21277d95b82a80b1ed2462688f.png",
        "http://localhost:3845/assets/a3a3894cd595828db65c63f212254fb42f9ae15f.png",
        "http://localhost:3845/assets/3ac94099cac41625b8b2d170d54c966e91f4454c.png",
        "http://localhost:3845/assets/55e354834c44c5a8475e875dab3345e391a29ea2.png",
        "http://localhost:3845/assets/a51fc4d57215f637b669c0a6ff7943a742c1e8eb.png"
    ],
    2: [
        "http://localhost:3845/assets/ce33565e2792df41ed4c47ef917708b2301b4a8f.png",
        "http://localhost:3845/assets/d5680f56c42c503d9f94798412222d67fd3dd4ac.png",
        "http://localhost:3845/assets/7b058a5d6fa723fe3cc2edff2040da5189c08da9.png"
    ],
    3: [
        "http://localhost:3845/assets/f73859a94fdfe6816bbeea92061d1ab7de13b050.png",
        "http://localhost:3845/assets/97f56deab3b2c0fa538d2f6da2c7125f686484e5.png",
        "http://localhost:3845/assets/b100ff114477be4bfe6c6a86072f8272f86d7ff8.png",
        "http://localhost:3845/assets/571226914f97ee3011fd0237419baca87ac4a77d.png",
        "http://localhost:3845/assets/fdb7d5feb2f50f0b734d9727a8c6fc49ff238d9a.png",
        "http://localhost:3845/assets/2a22dae4c868168c822b730bc6923fac7c4f5613.png"
    ],
    4: [
        "http://localhost:3845/assets/a53160367c98552bc731740b8c295513c8cb0de9.png",
        "http://localhost:3845/assets/fba5e38e84bf832bc77e101bbd931292d409df3f.png",
        "http://localhost:3845/assets/392932c6a1431d52e68550936a7695813c59ba29.png",
        "http://localhost:3845/assets/3d1d64e4d3c82519378804ebee90ab2424357c67.png",
        "http://localhost:3845/assets/a6442582f78d00343b26d3b36b458cc745bdee5f.png"
    ],
    5: [
        "http://localhost:3845/assets/ba0d4ca455cf4d403f93dfcd0bfa27ae8d29d810.png",
        "http://localhost:3845/assets/ad69b1584b7a3e383cad0d1a73142caacf7751bb.png",
        "http://localhost:3845/assets/a2ddf72528f1082de126c0f6941a1ad274b6fc8a.png",
        "http://localhost:3845/assets/a9b9eb9e48365c5e8f950f5b09ce4f98064c4e25.png",
        "http://localhost:3845/assets/f4fe059873f75fc50fa313213a9efe2a672e4a92.png",
        "http://localhost:3845/assets/0933b968949c3c3853ff5536d5f4148171d60bb7.png",
        "http://localhost:3845/assets/0de9cf2777dab45860a5e9931011cbae8072f046.png"
    ],
    6: [
        "http://localhost:3845/assets/e1cb0364ff839354e7a5661b77bf700716d05b4b.png",
        "http://localhost:3845/assets/8e3f3952393e6a57417646d142c420c6003c39e9.png",
        "http://localhost:3845/assets/b177f92b539a4411f26f665b44ac30feaca3aecb.png",
        "http://localhost:3845/assets/02250ac97a49d8f777d63d5ae30a142197852b84.png",
        "http://localhost:3845/assets/e1048ec1528afea7ed2bb083b48c44a3e9d1ee99.png",
        "http://localhost:3845/assets/e783fd1466160e347df774e2c7b9e2947a1402ce.png",
        "http://localhost:3845/assets/3002cbb52facc30bf3ce49c04575d8854441d595.png",
        "http://localhost:3845/assets/7747b4243d83d14c8aea6052ae169e5798d48dc5.png"
    ],
    7: [
        "http://localhost:3845/assets/0594247f12e2c56bb7178c7774287829775339c0.png"
    ],
    8: [
        "http://localhost:3845/assets/138dfd53595d456a99b546cb28ac20065f00d52f.png",
        "http://localhost:3845/assets/5dbbfdb91b5582c3b1e51005c8f5c990b5699798.png",
        "http://localhost:3845/assets/343f62c06c3d9c9c2330764baaa74b14e53450e9.png",
        "http://localhost:3845/assets/a04a3abab2d65e99377a009f651043eaee336351.png"
    ],
    9: [
        "http://localhost:3845/assets/51683465bdb44f152c9fa64851934982b4bc7342.png",
        "http://localhost:3845/assets/e6be8a7c0251b0bc61cb6e608bc838e4b35c7989.png",
        "http://localhost:3845/assets/8a510f3c4592040ac043fee4f80aee959c3292ee.png",
        "http://localhost:3845/assets/3dc41b3320af4ee755f919c3df285961d3fb999b.png",
        "http://localhost:3845/assets/740f781ac17cf6d64acaa3c3254df36424ac66c4.png",
        "http://localhost:3845/assets/73e2a23eaf503d2f91fbc54c55e4632c8983608e.png",
        "http://localhost:3845/assets/73c25f387584fc57923fd01caf8f68956dcf9c4b.png",
        "http://localhost:3845/assets/9198e225c8091ae3253523aa805023b41510525d.png"
    ],
    10: [
        "http://localhost:3845/assets/e3495b065a66ba80e5fb51bb5ae169e3a4c6bbc0.png",
        "http://localhost:3845/assets/9af57436fcf485af4668d8b493808d644019de9a.png",
        "http://localhost:3845/assets/a2ac8f7870799c584443a5767541922021f77004.png",
        "http://localhost:3845/assets/ff397ff30ac6fcef7322bb38debcbd293ec6cb4c.png",
        "http://localhost:3845/assets/24c66e6bbff6cfd10dae70b47ec941a7279a0c73.png",
        "http://localhost:3845/assets/4e8bd0476fd3a1267aa99a08b7424eac1c720fab.png"
    ]
}

# Base directory for assets
base_dir = r"c:\Users\Nuocdaidongchai\Documents\code\theonguyenprofile\web\assets\images\projects"

project_local_images = {}

for pid, urls in projects_assets.items():
    project_local_images[pid] = []
    for i, url in enumerate(urls):
        filename = f"img_{i+1}.png"
        path = os.path.join(base_dir, f"p{pid}", filename)
        download_image(url, path)
        project_local_images[pid].append(f"../assets/images/projects/p{pid}/{filename}")

# Detailed Content
projects_detailed = [
    {
        "id": 1,
        "title": "Artworks & Posters",
        "year": "2019 - 2024",
        "type": "Personal & Commission",
        "scope": "Visual Storytelling, Graphic Design",
        "description": "This project is a curated collection of poster designs and digital artworks created over the years. Each piece explores different visual languages, from minimalist typography to rich, experimental illustrations. Through these posters, I aim to communicate complex narratives and emotions using bold colors, striking imagery, and intentional compositions. This ongoing series serves as a creative playground where I refine my skills and explore new artistic directions.",
        "images": project_local_images[1],
        "bgColor": "#FE45EE"
    },
    {
        "id": 2,
        "title": "Logos & Marks",
        "year": "2021 - Now",
        "type": "Commission & Personal",
        "scope": "Visual Identity",
        "description": "The objective of this project was to develop logo systems that are visually refined, strategically grounded, and aligned with each client\u2019s brand positioning. Beyond aesthetics, the focus was on creating practical and scalable identities that clearly communicate brand values and support long-term business goals. By balancing form and function, these marks are designed to leave a lasting impact across various touchpoints, ensuring a consistent and professional brand presence.",
        "images": project_local_images[2],
        "bgColor": "#FE45EE"
    },
    {
        "id": 3,
        "title": "Len Huong",
        "year": "2020",
        "type": "Personal",
        "scope": "Zine Design, Visual Storytelling",
        "description": "\u2018Len Huong\u2019 is an art project that captures the essence of childhood memories and the nostalgic beauty of traditional Vietnamese festivals. Through a series of zines and illustrations, the project reimagines familiar cultural symbols \u2013 from lanterns to folk games \u2013 using a contemporary, experimental visual language. The goal was to create a sensory experience that evokes a sense of wonder and connection to heritage, blending personal storytelling with cultural preservation. Each piece is a celebration of the vibrant colors and timeless spirit of Vietnam, inviting viewers to revisit the joy of their own past.",
        "images": project_local_images[3],
        "bgColor": "#FE45EE"
    },
    {
        "id": 4,
        "title": "What Remains",
        "year": "2021 - 2023",
        "type": "Personal",
        "scope": "Photo Zine, Storytelling",
        "description": "\u2018What Remains\u2019 is an experimental photo zine exploring the concept of isolation and memory through the lens of abandoned architectural spaces. The project documentation captures the quiet, often overlooked details of decay, finding beauty in the stillness of forgotten environments. By pairing evocative photography with minimalist layouts, the zine creates a meditative journey that questions what we leave behind and how space holds onto the echoes of human presence. The intentional use of negative space and muted tones enhances the sense of solitude, inviting a deeper reflection on the passage of time and the fragility of our surroundings.",
        "images": project_local_images[4],
        "bgColor": "#FE45EE"
    },
    {
        "id": 5,
        "title": "Today U Wear",
        "year": "2023 - Now",
        "type": "Commission",
        "scope": "Art Direction, Brand Repositioning & Strategy, Product Design (Apparel), Social Media Posts",
        "description": "This project supported Today U Wear (TUW), one of Hanoi\u2019s first premium local sportswear brands, in reconnecting with its audience and repositioning itself as a leader in the athleisure market by blending performance-driven gym wear with everyday style. Facing the challenge of rebuilding brand trust and visibility in a saturated market, I served as Art Director and Designer, leading the visual identity refresh and campaign direction. Since December 2023, the new bold, friendly, and energetic visual system has driven TUW\u2019s rapid return to market leadership.",
        "images": project_local_images[5],
        "bgColor": "#FE45EE"
    },
    {
        "id": 6,
        "title": "Di Luon Khong",
        "year": "2024",
        "type": "Non-profit",
        "scope": "Design Direction, Brand Identity & Positioning, Illustration",
        "description": "This project focused on building a community-driven podcast positioned as an accessible cultural platform, inviting audiences to \u201ctake a stroll\u201d through personal narratives, friendships, and underrepresented perspectives of urban life. The identity system was designed to be distinctive yet flexible, combining bold typography, hand-drawn illustrations, and a solid color palette inspired by Hanoi\u2019s streets and everyday environments.",
        "images": project_local_images[6],
        "bgColor": "#FE45EE"
    },
    {
        "id": 7,
        "title": "Micro Animation",
        "year": "2024",
        "type": "Personal & Commission",
        "scope": "Micro Animation, Lottie Files Handling",
        "description": "Working within tech and software environments shaped my approach to motion as a strategic design tool rather than a decorative layer. Micro-animations demand a deep understanding of user behavior. The challenge is knowing when motion adds value, and when restraint matters more. By combining thoughtful interaction design with intentional motion, I craft web and mobile experiences that are seamless, intuitive, and emotionally resonant.",
        "images": project_local_images[7],
        "bgColor": "#FE45EE"
    },
    {
        "id": 8,
        "title": "The Horse",
        "year": "2025",
        "type": "Personal",
        "scope": "Zine Design",
        "description": "During my studies in CalArts\u2019 Graphic Design specialization, the final assignment for the Image Making course challenged students to communicate a personal, emotionally driven narrative through experimental imagery. I developed a zine that functions as a visual metaphor for my internal state at the time: a restless horse drawn toward freedom while constrained by emotional weight.",
        "images": project_local_images[8],
        "bgColor": "#FE45EE"
    },
    {
        "id": 9,
        "title": "Ukiyo Sushi Bar",
        "year": "2026",
        "type": "Personal",
        "scope": "Art Direction, Brand Identity & Positioning, Spatial Design Concept",
        "description": "UKIYO (\u6d6e\u4e16), a Tokyo-based sushi restaurant, was envisioned as more than a dining destination, but also a curated sensory retreat where culinary precision, intimate soundscapes, and collectible art converge. The design approach embraces restraint and intentionality - minimal yet profound - drawing from Japanese culture and Taoist philosophy of stillness.",
        "images": project_local_images[9],
        "bgColor": "#FE45EE"
    },
    {
        "id": 10,
        "title": "Vinamilk Works",
        "year": "2026",
        "type": "Commission",
        "scope": "Branding & Packaging",
        "description": "A comprehensive branding and packaging project for Vinamilk's new range of premium dairy products. The focus was on creating a modern, fresh, and trustworthy visual language that stands out on the shelf and resonates with health-conscious consumers. The project involved redesigning core brand elements to emphasize natural quality and heritage.",
        "images": project_local_images[10],
        "bgColor": "#FE45EE"
    }
]

js_content = f"const projectsData = {json.dumps(projects_detailed, indent=2)};\n\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = projectsData;\n}}\n"

with open(r"c:\Users\Nuocdaidongchai\Documents\code\theonguyenprofile\web\works\projects-data.js", "w", encoding='utf-8') as f:
    f.write(js_content)

print("Project data updated and images downloaded.")
