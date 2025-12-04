Last spring, when Veo 3 came out, I was stunned. It was clear we’d crossed a crucial threshold in video generation. I began thinking of what I could build on top of it. I workshopped some consumer apps revolving around choose-your-own-adventure video, but felt the quality of video that was being produced, even by SOTA models like Veo3, was still sloppy, and orders of magnitude too slow for a snappy video game-like experience. That being said, I’m positive something like AI Dungeon with video will be a massive hit in the near future.

What I landed on was the part of cinema that is already synthetic: visual effects. I began working on a text-to-FX tool that would output EXRs ready to be composited. 

The VFX process works more-or-less as follows. Say you want a car blowing up. You’ll start by creating an explosion in a 3D software like Houdini. Once your explosion looks right, you render it as a 2D "video", which then gets brought into a compositing software like Nuke, which allows you to combine the CGI explosion with the real footage in a way that appears natural. (In reality you’re combining multiple videos of the explosion — you’d have a depth pass, that shows how far each point is from the camera (which allows you to match the focus blur), a specular pass, which allows you to match highlights, etc. All these layers are bundled in a file type called EXR.)

What I wanted to build was a tool that would allow the artist to import their raw footage + mask of where the effect should go, import a still of few seconds of the effect they want, and get an EXR with crucial passes of the effect.

At first I was working with Hunyuan video, which was at the time considered the best open-source video model, but that didn’t give me the flexibility I wanted, so I moved on to Alibaba's Wan2.1. That was better, the model is built to be used with controlnets but still not flexible enough: the it is very good at, say, adding an explosion that sylistically matches the footage, but that wouldn’t allow me to extract the “intact” passes of the effect a compositor needs.

I then switched to AnimateDiff, which is a tweak to StableDiffusion that allows it to generate video. It uses the older U-net architecture, but the huge upside is its vibrant community: you can use model checkpoints for StableDiffusion, and there are a lot of tools to train LoRAs, Controlnets, etc. I trained spatial / motion LoRAs with [MotionDirector](https://github.com/ExponentialML/AnimateDiff-MotionDirector), and a spatial LoRA with [kohya_ss](https://github.com/bmaltais/kohya_ss).

To get the EXR, I started working on what I pretty much knew from the start was a doomed venture: extracting high-resolution passes from ai-generated footage. There was too much variability to get a high-quality EXR that would be usable in professional setting.

The nail in the coffin was Runway’s Aleph. [This](assets/comfyui/sd15_inpainting_controlnet_upscale.json) was my final ComfyUI workflow.

Rumour has it Meta is currently working on a similar project at a massive scale. From the Reddit threads discussing it, they seem to be doing a pretty messy job of it, it doesn’t sound as if they have too many FX people calling the shots. Will be interested in seeing what comes of that.

Some questions I still have after this project:
How do you generate against a blank background? Preconditioning the latent + adding an area mask was alright, but it ended up incorporating the latent’s colour into the effect (e.g., an explosion on the tan background would have wisps of tan in it, as if the explosion was happening in the desert). Also, using a green or blue latent just produced garbage.

Where will the industry go? I think we’ll have a very split landscape: big-budget productions will keep using, maybe with generative AI for background effects. 