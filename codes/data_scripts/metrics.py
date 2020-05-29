import re
import sys

metric = '((-)*[0-9]\.[0-9]+e[\-\+][0-9]+)'
iter_number = r' iter:[ ]*([0-9]+[,]*[0-9]+)'
l_g_pix = ''.join([r'l_g_pix: ', metric])
l_g_fea = ''.join([r'l_g_fea: ', metric])
l_g_gan = ''.join([r'l_g_gan: ', metric])
l_d_real = ''.join([r'l_d_real: ', metric])
l_d_fake = ''.join([r'l_d_fake: ', metric])
D_real = ''.join([r'D_real: ', metric])
D_fake = ''.join([r'D_fake: ', metric])
psnr = ''.join([r'PSNR: ', metric])


with open(sys.argv[1]) as log:
    csv = open('metrics.csv', 'w')
    csv.write(','.join(['iter', 'l_g_pix', 'l_g_fea', 'l_g_gan', 'l_d_real', 'l_d_fake', 'D_real', 'D_fake']))
    csv.write('\n')
    content = log.read()
    i_it = re.finditer(iter_number, content)
    l_g_pix_it = re.finditer(l_g_pix, content)
    l_g_fea_it = re.finditer(l_g_fea, content)
    l_g_gan_it = re.finditer(l_g_gan, content)
    l_d_real_it = re.finditer(l_d_real, content)
    l_d_fake_it = re.finditer(l_d_fake, content)
    D_real_it = re.finditer(D_real, content)
    D_fake_it = re.finditer(D_fake, content)
    for i, a, b, c, d, e, f, g in zip(i_it,
                                      l_g_pix_it,
                                      l_g_fea_it,
                                      l_g_gan_it,
                                      l_d_real_it,
                                      l_d_fake_it,
                                      D_real_it,
                                      D_fake_it):
        csv.write(','.join([i.group(1).replace(',', ''),
                            a.group(1),
                            b.group(1),
                            c.group(1),
                            d.group(1),
                            e.group(1),
                            f.group(1),
                            g.group(1)]))
        csv.write('\n')
    csv.close()

    with open('psnr.csv', 'w') as psnr_log:
        psnr_log.write('PSNR')
        psnr_log.write('\n')
        for p in re.finditer(psnr, content):
            psnr_log.write(p.group(1))
            psnr_log.write('\n')
