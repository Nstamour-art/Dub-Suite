from demucs import pretrained
from demucs.apply import apply_model
import torchaudio


class DemucsSFXSeparator:
    def __init__(self):
        self.model = pretrained.get_model("demucs")

    def separate(self, audio_path: str):
        """Separate audio into stems using Demucs model."""
        wav, sr = torchaudio.load(audio_path)
        sources = apply_model(self.model, wav.unsqueeze(0), device="cpu")
        sfx_output_path = audio_path.replace(".wav", "_sfx.wav")
        vocals_output_path = audio_path.replace(".wav", "_vocals.wav")
        # Save the separated tracks (sources contains drums, bass, other, vocals)
        torchaudio.save(sfx_output_path, sources[0, 2], sr)  # 'other' stem for SFX
        torchaudio.save(vocals_output_path, sources[0, 3], sr)  # 'vocals' stem
        return sfx_output_path, vocals_output_path
