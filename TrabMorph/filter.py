import numpy as np

def morph_filter(mode:str, img:np.ndarray, kernel:np.ndarray, pad_val:float = 0):
    if mode == "open":
        result = morph_filter('erode', img, kernel, pad_val)
        return morph_filter('dilate', result, kernel, pad_val)
    elif mode == "close":
        result = morph_filter('dilate', img, kernel, pad_val)
        return morph_filter('erode', img, kernel, pad_val)
    
    off = kernel.shape[0] // 2
    padded = np.pad(img, (off, off), 'constant', constant_values=pad_val)

    h, w = padded.shape[0], padded.shape[1]
    copy = img.copy()

    # for row in range(kernel.shape[0] // 2, h - kernel.shape[0] // 2):
    #     for col in range(kernel.shape[0] // 2, w - kernel.shape[0] // 2):
    #         slice = padded[row - kernel.shape[0] // 2 : row + kernel.shape[0] // 2 + 1, col - kernel.shape[0] // 2 : col + kernel.shape[0] // 2 + 1].flatten()

    for row in range(off, h - off):
        for col in range(off, w - off):
            slice = padded[row - off : row + off + 1, col - off : col + off + 1]
            pixels = []
            for i in range(0, len(slice)):
                for j in range(0, len(slice)):
                    if kernel[i,j] != 0: pixels.append(slice[i,j])

            count = 0
            count = len(list(filter(lambda p: p > 0, pixels)))


            if mode == 'erode':
                n = len(pixels)
                validation = count >= n
            if mode == 'dilate':
                validation = count > 0

            if validation:
                copy[row - off][col - off] = 255
            else:
                copy[row - off][col - off] = 0

    return copy


def threshold(img, val):
    out = img.copy()
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            out = 0xff if img[i][j] >= val else 0x00
    return out


