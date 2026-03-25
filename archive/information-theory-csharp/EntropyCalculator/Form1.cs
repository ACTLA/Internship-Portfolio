using System;
using System.Drawing;
using System.Windows.Forms;


namespace EntropyCalculator
{
    public partial class Form1 : System.Windows.Forms.Form
    {
        public Form1()
        {
            InitializeComponents(); 
            //BallQuantityManualModeRadioButton.CheckedChanged += new EventHandler(ManualModeRadioButton_CheckedChanged);
        }



        private void RandomModeRadioButton_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void ProgramDescriptionLabel_Click(object sender, EventArgs e)
        {

        }

        private void BallQuantitySelectionModeRequestLabel_Click(object sender, EventArgs e)
        {

        }

        private void ManualModeRadioButton_CheckedChanged(object sender, EventArgs e)
        {   
        if (BallQuantityManualModeRadioButton.Checked)
        {
            TotalBallQuantityRequestLabel.Visible = true; // Показываем Label
        }
        else
        {
            TotalBallQuantityRequestLabel.Visible = false; // Скрываем Label
        }
            //Label TotalBallQuantityRequestLabel = new Label();
            //TotalBallQuantityRequestLabel.AutoSize = true;
            //TotalBallQuantityRequestLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            //TotalBallQuantityRequestLabel.Location = new System.Drawing.Point(582, 178);
            //TotalBallQuantityRequestLabel.Name = "TotalBallQuantityRequestLabel";
            //TotalBallQuantityRequestLabel.Size = new System.Drawing.Size(349, 25);
            //TotalBallQuantityRequestLabel.TabIndex = 11;
            //TotalBallQuantityRequestLabel.Text = "Укажите общее количество шаров: ";
            //TotalBallQuantityRequestLabel.Visible = true;
            
            //if (BallQuantityManualModeRadioButton.Checked)
            //{
            //    Controls.Add(TotalBallQuantityRequestLabel);
            //}
            //else
            //{
            //    TotalBallQuantityRequestLabel.Visible = false;
            //    Controls.Remove(TotalBallQuantityRequestLabel);
            //    TotalBallQuantityRequestLabel.Dispose();
            //    TotalBallQuantityRequestLabel = null;
            //}
        }
  /*            this.TotalBallQuantityRequestLabel.AutoSize = true;
            this.TotalBallQuantityRequestLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.TotalBallQuantityRequestLabel.Location = new System.Drawing.Point(582, 178);
            this.TotalBallQuantityRequestLabel.Name = "TotalBallQuantityRequestLabel";
            this.TotalBallQuantityRequestLabel.Size = new System.Drawing.Size(349, 25);
            this.TotalBallQuantityRequestLabel.TabIndex = 11;
            this.TotalBallQuantityRequestLabel.Text = "Укажите общее количество шаров: ";
            this.TotalBallQuantityRequestLabel.Visible = false;
            this.TotalBallQuantityRequestLabel.Click += new System.EventHandler(this.label2_Click);*/
        private void BallTypesQuantityTextBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void BallTypesQuantityRequestLabel_Click(object sender, EventArgs e)
        {

        }

        private void BallTypesQuantityNumericUpDown_ValueChanged(object sender, EventArgs e)
        {

        }

        private void ParametersInfoRichTextBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void BallTypesQuantitySendButton_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }
        
        private void BallDistributionRequestLabel_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void InitializeComponents()
        {
            //
            // ParametersInfoRichTextBox
            //
            ParametersInfoRichTextBox = new System.Windows.Forms.RichTextBox
            {
                Name = "ParametrsInfoRichTextBox",
                Enabled = false,
                Location = new System.Drawing.Point(10, 40),
                Size = new System.Drawing.Size(500, 500),
                BackColor = System.Drawing.Color.White,
                BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D,
                ReadOnly = true,
                TabStop = false,
                Text = "",
            };
            //
            // TotalBallQuantityRequestLabel
            //
            TotalBallQuantityRequestLabel = new System.Windows.Forms.Label
            {
                AutoSize = true,
                Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204))),
                Location = new System.Drawing.Point(550, 140),
                Name = "TotalBallQuantityRequestLabel",
                //Size = new System.Drawing.Size(349, 25),
                //TabIndex = 11,
                Text = "Укажите общее количество шаров: ",
                Visible = false // Изначально скрыт
            };
            //
            // ProgramDescription
            //
            ProgramDescriptionLabel = new System.Windows.Forms.Label
            {
                //AutoSize = true,
                BackColor = System.Drawing.Color.Transparent,
                Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204))),
                Location = new System.Drawing.Point(15, 10),
                Name = "ProgramDescriptionLabel",
                Size = new System.Drawing.Size(1000, 20),
                Text = "Программа подсчета энтропии для указанного количества шаров в урне.",
                TextAlign = System.Drawing.ContentAlignment.TopCenter
            };
            //
            // BallTypesQuantityRequestLabel
            //
            BallTypesQuantityRequestLabel = new System.Windows.Forms.Label
            {
                AutoSize = true,
                BackColor = System.Drawing.Color.Transparent,
                Location = new System.Drawing.Point(550, 40),
                Size = new System.Drawing.Size(20, 20),
                Text = "Укажите количество видов шаров: ",
                Name = "BallTypesQuantityRequestLabel",
                Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (byte)(204))
            };
            //
            // BallTypesQuantityNumericUpDown
            //
            BallTypesQuantityNumericUpDown = new System.Windows.Forms.NumericUpDown
            {
                Location = new System.Drawing.Point(830, 40),
                Name = "BallTypesQuantityNumericUpDown", 
                AutoSize = true,
                Size = new System.Drawing.Size(50, 20),
                Maximum = new decimal(new int[] {99, 0, 0, 0}),
                TabStop = false,
            };
            //
            // BallTypesQuantitySendButton
            //
            BallTypesQuantitySendButton = new System.Windows.Forms.Button()
            {
                BackColor = System.Drawing.Color.Transparent,           
                Location = new System.Drawing.Point(900, 40),
                Size = new System.Drawing.Size(40, 20),
                Name = "BallTypesQuantitySendButton", 
                Text = "Ввести",
                AutoSize = true,
                TabStop = false,
            };
            //
            // BallQuantitySelectionModeRequestLabel
            //
            BallQuantitySelectionModeRequestLabel = new System.Windows.Forms.Label()
            {
                BackColor = System.Drawing.Color.Transparent,
                Location = new System.Drawing.Point(550, 70),
                Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (byte)(204)),
                Text = "Как хотите указать общее количество шаров?",
                Name = "BallQuantitySelectionModeRequestLabel",
                AutoSize = true,
            };
            //
            // BallQuantityRandomModeRadioButton
            //
            BallQuantityRandomModeRadioButton = new System.Windows.Forms.RadioButton()
            {
                BackColor = System.Drawing.Color.Transparent,
                Location = new System.Drawing.Point(600, 100),
                Text = "случайно",
                Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, GraphicsUnit.Point, (byte)(204)),
                Size = new System.Drawing.Size(100, 30),
                Name = "BallQuantityRandomModeRadioButton",

            };
            //
            // TotalBallQuantityNumericUpDown
            //
            TotalBallQuantityNumericUpDown = new System.Windows.Forms.NumericUpDown()
            {
                Location = new System.Drawing.Point(832, 140),
                Size = new System.Drawing.Size(50, 20),
                Name = "TotalBallQuantityNumericUpDown",
                AutoSize = true,
                Maximum = new decimal(new int[] { 500, 0, 0, 0 }),
                TabStop = false,
                Visible = false,
            };
            //
            // BallQuantityManualModeRadioButton
            //
            BallQuantityManualModeRadioButton = new RadioButton()
            {
                BackColor = System.Drawing.Color.Transparent,
                Location = new System.Drawing.Point(780, 100),
                Text = "вручную",
                Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, GraphicsUnit.Point, (byte)(204)),
                Size = new System.Drawing.Size(100, 30),
                Name = "BallQuantityManualModeRadioButton",
            };
            //
            // TotalBallQuantitySendButton
            //
            TotalBallQuantitySendButton = new System.Windows.Forms.Button()
            {
                BackColor = System.Drawing.Color.Transparent,
                Location = new System.Drawing.Point(900, 140),
                Size = new System.Drawing.Size(40, 20),
                Name = "TotalBallQuantitySendButton",
                Text = "Ввести",
                AutoSize = true,
                TabStop = false,
                Visible = false,
            };
            //
            // Form1
            //
            AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            ClientSize = new System.Drawing.Size(1000, 1000);
            MinimumSize = new System.Drawing.Size(600, 600);
            Name = "Form1";
            Text = "EntropyCalculator";
            Controls.Add(ProgramDescriptionLabel);
            Controls.Add(ParametersInfoRichTextBox);
            Controls.Add(BallTypesQuantityRequestLabel);
            Controls.Add(BallTypesQuantityNumericUpDown);
            Controls.Add(BallTypesQuantitySendButton);
            Controls.Add(BallQuantitySelectionModeRequestLabel);
            Controls.Add(BallQuantityRandomModeRadioButton);
            Controls.Add(BallQuantityManualModeRadioButton);
            Controls.Add(TotalBallQuantityRequestLabel);
            Controls.Add(TotalBallQuantityNumericUpDown);
            Controls.Add(TotalBallQuantitySendButton);
            ResumeLayout(false);
            PerformLayout();
        }

        private System.Windows.Forms.Label TotalBallQuantityRequestLabel;
        private System.Windows.Forms.RadioButton BallQuantityRandomModeRadioButton;
        private System.Windows.Forms.RadioButton BallQuantityManualModeRadioButton;
        private System.Windows.Forms.Label ProgramDescriptionLabel;
        private System.Windows.Forms.Label BallQuantitySelectionModeRequestLabel;
        private System.Windows.Forms.Label BallTypesQuantityRequestLabel;
        private System.Windows.Forms.Button BallTypesQuantitySendButton;
        private System.Windows.Forms.RichTextBox ParametersInfoRichTextBox;
        private System.Windows.Forms.NumericUpDown BallTypesQuantityNumericUpDown;
        private System.Windows.Forms.NumericUpDown TotalBallQuantityNumericUpDown;
        private System.Windows.Forms.Button TotalBallQuantitySendButton;
        private System.Windows.Forms.Label BallDistributionRequestLabel;
        private System.Windows.Forms.RadioButton BallDistributionRandomModeRadioButton;
        private System.Windows.Forms.RadioButton BallDistributionManualModeRadioButton;
        private System.Windows.Forms.Label OneTypeBallQuantityRequestLabel;
        private System.Windows.Forms.NumericUpDown OneTypeBallQuantityNumericUpDown;

        private void InitializeComponent()
        {
            this.SuspendLayout();
            // 
            // Form1
            // 
            this.ClientSize = new System.Drawing.Size(278, 244);
            this.Name = "Form1";
            this.ResumeLayout(false);

        }
    }
}

/*
namespace EntropyCalculator
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.BallQuantityRandomModeRadioButton = new System.Windows.Forms.RadioButton();
            this.BallQuantityManualModeRadioButton = new System.Windows.Forms.RadioButton();
            this.ProgramDescriptionLabel = new System.Windows.Forms.Label();
            this.BallQuantitySelectionModeRequestLabel = new System.Windows.Forms.Label();
            this.BallTypesQuantityRequestLabel = new System.Windows.Forms.Label();
            this.BallTypesQuantitySendButton = new System.Windows.Forms.Button();
            this.ParametersInfoRichTextBox = new System.Windows.Forms.RichTextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.BallTypesQuantityNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.TotalBallQuantityNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.TotalBallQuantitySendButton = new System.Windows.Forms.Button();
            this.BallDistributionRequestLabel = new System.Windows.Forms.Label();
            this.BallDistributionRandomModeRadioButton = new System.Windows.Forms.RadioButton();
            this.BallDistributionManualModeRadioButton = new System.Windows.Forms.RadioButton();
            this.OneTypeBallQuantityRequestLabel = new System.Windows.Forms.Label();
            this.OneTypeBallQuantityNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.BallTypesQuantityNumericUpDown)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.TotalBallQuantityNumericUpDown)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.OneTypeBallQuantityNumericUpDown)).BeginInit();
            this.SuspendLayout();
            // 
            // BallQuantityRandomModeRadioButton
            // 
            this.BallQuantityRandomModeRadioButton.AutoSize = true;
            this.BallQuantityRandomModeRadioButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.BallQuantityRandomModeRadioButton.Location = new System.Drawing.Point(630, 134);
            this.BallQuantityRandomModeRadioButton.Name = "BallQuantityRandomModeRadioButton";
            this.BallQuantityRandomModeRadioButton.Size = new System.Drawing.Size(122, 29);
            this.BallQuantityRandomModeRadioButton.TabIndex = 0;
            this.BallQuantityRandomModeRadioButton.TabStop = true;
            this.BallQuantityRandomModeRadioButton.Text = "случайно";
            this.BallQuantityRandomModeRadioButton.UseVisualStyleBackColor = true;
            this.BallQuantityRandomModeRadioButton.CheckedChanged += new System.EventHandler(this.RandomModeRadioButton_CheckedChanged);
            // 
            // BallQuantityManualModeRadioButton
            // 
            this.BallQuantityManualModeRadioButton.AutoSize = true;
            this.BallQuantityManualModeRadioButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.BallQuantityManualModeRadioButton.Location = new System.Drawing.Point(802, 134);
            this.BallQuantityManualModeRadioButton.Name = "BallQuantityManualModeRadioButton";
            this.BallQuantityManualModeRadioButton.Size = new System.Drawing.Size(113, 29);
            this.BallQuantityManualModeRadioButton.TabIndex = 1;
            this.BallQuantityManualModeRadioButton.TabStop = true;
            this.BallQuantityManualModeRadioButton.Text = "вручную";
            this.BallQuantityManualModeRadioButton.UseVisualStyleBackColor = true;
            this.BallQuantityManualModeRadioButton.CheckedChanged += new System.EventHandler(this.ManualModeRadioButton_CheckedChanged);
            // 
            // ProgramDescriptionLabel
            // 
            this.ProgramDescriptionLabel.BackColor = System.Drawing.Color.Transparent;
            this.ProgramDescriptionLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.ProgramDescriptionLabel.Location = new System.Drawing.Point(177, 9);
            this.ProgramDescriptionLabel.Name = "ProgramDescriptionLabel";
            this.ProgramDescriptionLabel.Size = new System.Drawing.Size(776, 25);
            this.ProgramDescriptionLabel.TabIndex = 2;
            this.ProgramDescriptionLabel.Text = "Программа подсчета энтропии для указанного количества шаров в урне.";
            this.ProgramDescriptionLabel.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.ProgramDescriptionLabel.Click += new System.EventHandler(this.ProgramDescriptionLabel_Click);
            // 
            // BallQuantitySelectionModeRequestLabel
            // 
            this.BallQuantitySelectionModeRequestLabel.AutoSize = true;
            this.BallQuantitySelectionModeRequestLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.BallQuantitySelectionModeRequestLabel.Location = new System.Drawing.Point(582, 93);
            this.BallQuantitySelectionModeRequestLabel.Name = "BallQuantitySelectionModeRequestLabel";
            this.BallQuantitySelectionModeRequestLabel.Size = new System.Drawing.Size(447, 25);
            this.BallQuantitySelectionModeRequestLabel.TabIndex = 3;
            this.BallQuantitySelectionModeRequestLabel.Text = "Как хотите указать общее количество шаров?";
            this.BallQuantitySelectionModeRequestLabel.Click += new System.EventHandler(this.BallQuantitySelectionModeRequestLabel_Click);
            // 
            // BallTypesQuantityRequestLabel
            // 
            this.BallTypesQuantityRequestLabel.AutoSize = true;
            this.BallTypesQuantityRequestLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.BallTypesQuantityRequestLabel.Location = new System.Drawing.Point(582, 54);
            this.BallTypesQuantityRequestLabel.Name = "BallTypesQuantityRequestLabel";
            this.BallTypesQuantityRequestLabel.Size = new System.Drawing.Size(342, 25);
            this.BallTypesQuantityRequestLabel.TabIndex = 4;
            this.BallTypesQuantityRequestLabel.Text = "Укажите количество видов шаров: ";
            this.BallTypesQuantityRequestLabel.Click += new System.EventHandler(this.BallTypesQuantityRequestLabel_Click);
            // 
            // BallTypesQuantitySendButton
            // 
            this.BallTypesQuantitySendButton.BackColor = System.Drawing.Color.Transparent;
            this.BallTypesQuantitySendButton.Image = ((System.Drawing.Image)(resources.GetObject("BallTypesQuantitySendButton.Image")));
            this.BallTypesQuantitySendButton.Location = new System.Drawing.Point(1043, 46);
            this.BallTypesQuantitySendButton.Name = "BallTypesQuantitySendButton";
            this.BallTypesQuantitySendButton.Size = new System.Drawing.Size(45, 44);
            this.BallTypesQuantitySendButton.TabIndex = 7;
            this.BallTypesQuantitySendButton.UseVisualStyleBackColor = false;
            this.BallTypesQuantitySendButton.Click += new System.EventHandler(this.BallTypesQuantitySendButton_Click);
            // 
            // ParametersInfoRichTextBox
            // 
            this.ParametersInfoRichTextBox.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.ParametersInfoRichTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.ParametersInfoRichTextBox.Enabled = false;
            this.ParametersInfoRichTextBox.Location = new System.Drawing.Point(21, 54);
            this.ParametersInfoRichTextBox.Name = "ParametersInfoRichTextBox";
            this.ParametersInfoRichTextBox.ReadOnly = true;
            this.ParametersInfoRichTextBox.Size = new System.Drawing.Size(550, 286);
            this.ParametersInfoRichTextBox.TabIndex = 8;
            this.ParametersInfoRichTextBox.TabStop = false;
            this.ParametersInfoRichTextBox.Text = "";
            this.ParametersInfoRichTextBox.TextChanged += new System.EventHandler(this.ParametersInfoRichTextBox_TextChanged);
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.SystemColors.ButtonShadow;
            this.label1.Enabled = false;
            this.label1.Location = new System.Drawing.Point(13, 46);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(566, 302);
            this.label1.TabIndex = 9;
            // 
            // BallTypesQuantityNumericUpDown
            // 
            this.BallTypesQuantityNumericUpDown.Location = new System.Drawing.Point(945, 56);
            this.BallTypesQuantityNumericUpDown.Maximum = new decimal(new int[] {
            99,
            0,
            0,
            0});
            this.BallTypesQuantityNumericUpDown.Name = "BallTypesQuantityNumericUpDown";
            this.BallTypesQuantityNumericUpDown.Size = new System.Drawing.Size(80, 26);
            this.BallTypesQuantityNumericUpDown.TabIndex = 10;
            this.BallTypesQuantityNumericUpDown.ValueChanged += new System.EventHandler(this.BallTypesQuantityNumericUpDown_ValueChanged);
            // 
            // TotalBallQuantityNumericUpDown
            // 
            this.TotalBallQuantityNumericUpDown.Location = new System.Drawing.Point(945, 180);
            this.TotalBallQuantityNumericUpDown.Maximum = new decimal(new int[] {
            200,
            0,
            0,
            0});
            this.TotalBallQuantityNumericUpDown.Name = "TotalBallQuantityNumericUpDown";
            this.TotalBallQuantityNumericUpDown.Size = new System.Drawing.Size(80, 26);
            this.TotalBallQuantityNumericUpDown.TabIndex = 12;
            this.TotalBallQuantityNumericUpDown.Visible = false;
            // 
            // TotalBallQuantitySendButton
            // 
            this.TotalBallQuantitySendButton.BackColor = System.Drawing.Color.Transparent;
            this.TotalBallQuantitySendButton.Image = ((System.Drawing.Image)(resources.GetObject("TotalBallQuantitySendButton.Image")));
            this.TotalBallQuantitySendButton.Location = new System.Drawing.Point(1043, 170);
            this.TotalBallQuantitySendButton.Name = "TotalBallQuantitySendButton";
            this.TotalBallQuantitySendButton.Size = new System.Drawing.Size(45, 44);
            this.TotalBallQuantitySendButton.TabIndex = 13;
            this.TotalBallQuantitySendButton.UseVisualStyleBackColor = false;
            this.TotalBallQuantitySendButton.Visible = false;
            // 
            // BallDistributionRequestLabel
            // 
            this.BallDistributionRequestLabel.AutoSize = true;
            this.BallDistributionRequestLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.BallDistributionRequestLabel.Location = new System.Drawing.Point(595, 315);
            this.BallDistributionRequestLabel.Name = "BallDistributionRequestLabel";
            this.BallDistributionRequestLabel.Size = new System.Drawing.Size(320, 25);
            this.BallDistributionRequestLabel.TabIndex = 14;
            this.BallDistributionRequestLabel.Text = "Как хотите распределить шары?";
            this.BallDistributionRequestLabel.Visible = false;
            this.BallDistributionRequestLabel.Click += new System.EventHandler(this.BallDistributionRequestLabel_Click);
            // 
            // BallDistributionRandomModeRadioButton
            // 
            this.BallDistributionRandomModeRadioButton.AutoSize = true;
            this.BallDistributionRandomModeRadioButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.BallDistributionRandomModeRadioButton.Location = new System.Drawing.Point(630, 220);
            this.BallDistributionRandomModeRadioButton.Name = "BallDistributionRandomModeRadioButton";
            this.BallDistributionRandomModeRadioButton.Size = new System.Drawing.Size(122, 29);
            this.BallDistributionRandomModeRadioButton.TabIndex = 15;
            this.BallDistributionRandomModeRadioButton.TabStop = true;
            this.BallDistributionRandomModeRadioButton.Text = "случайно";
            this.BallDistributionRandomModeRadioButton.UseVisualStyleBackColor = true;
            this.BallDistributionRandomModeRadioButton.Visible = false;
            // 
            // BallDistributionManualModeRadioButton
            // 
            this.BallDistributionManualModeRadioButton.AutoSize = true;
            this.BallDistributionManualModeRadioButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.BallDistributionManualModeRadioButton.Location = new System.Drawing.Point(802, 220);
            this.BallDistributionManualModeRadioButton.Name = "BallDistributionManualModeRadioButton";
            this.BallDistributionManualModeRadioButton.Size = new System.Drawing.Size(113, 29);
            this.BallDistributionManualModeRadioButton.TabIndex = 16;
            this.BallDistributionManualModeRadioButton.TabStop = true;
            this.BallDistributionManualModeRadioButton.Text = "вручную";
            this.BallDistributionManualModeRadioButton.UseVisualStyleBackColor = true;
            this.BallDistributionManualModeRadioButton.Visible = false;
            // 
            // OneTypeBallQuantityRequestLabel
            // 
            this.OneTypeBallQuantityRequestLabel.AutoSize = true;
            this.OneTypeBallQuantityRequestLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.OneTypeBallQuantityRequestLabel.Location = new System.Drawing.Point(585, 259);
            this.OneTypeBallQuantityRequestLabel.Name = "OneTypeBallQuantityRequestLabel";
            this.OneTypeBallQuantityRequestLabel.Size = new System.Drawing.Size(347, 25);
            this.OneTypeBallQuantityRequestLabel.TabIndex = 17;
            this.OneTypeBallQuantityRequestLabel.Text = "Укажите количество шаров вида 1: ";
            this.OneTypeBallQuantityRequestLabel.Visible = false;
            this.OneTypeBallQuantityRequestLabel.Click += new System.EventHandler(this.label3_Click);
            // 
            // OneTypeBallQuantityNumericUpDown
            // 
            this.OneTypeBallQuantityNumericUpDown.Location = new System.Drawing.Point(945, 259);
            this.OneTypeBallQuantityNumericUpDown.Maximum = new decimal(new int[] {
            200,
            0,
            0,
            0});
            this.OneTypeBallQuantityNumericUpDown.Name = "OneTypeBallQuantityNumericUpDown";
            this.OneTypeBallQuantityNumericUpDown.Size = new System.Drawing.Size(80, 26);
            this.OneTypeBallQuantityNumericUpDown.TabIndex = 18;
            this.OneTypeBallQuantityNumericUpDown.Visible = false;
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.Transparent;
            this.button1.Image = ((System.Drawing.Image)(resources.GetObject("button1.Image")));
            this.button1.Location = new System.Drawing.Point(1043, 249);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(45, 44);
            this.button1.TabIndex = 19;
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1099, 470);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.OneTypeBallQuantityNumericUpDown);
            this.Controls.Add(this.OneTypeBallQuantityRequestLabel);
            this.Controls.Add(this.BallDistributionManualModeRadioButton);
            this.Controls.Add(this.BallDistributionRandomModeRadioButton);
            this.Controls.Add(this.BallDistributionRequestLabel);
            this.Controls.Add(this.TotalBallQuantitySendButton);
            this.Controls.Add(this.TotalBallQuantityNumericUpDown);
            this.Controls.Add(this.BallTypesQuantityNumericUpDown);
            this.Controls.Add(this.ParametersInfoRichTextBox);
            this.Controls.Add(this.BallTypesQuantitySendButton);
            this.Controls.Add(this.BallTypesQuantityRequestLabel);
            this.Controls.Add(this.BallQuantitySelectionModeRequestLabel);
            this.Controls.Add(this.ProgramDescriptionLabel);
            this.Controls.Add(this.BallQuantityManualModeRadioButton);
            this.Controls.Add(this.BallQuantityRandomModeRadioButton);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "EntropyCalculator";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.BallTypesQuantityNumericUpDown)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.TotalBallQuantityNumericUpDown)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.OneTypeBallQuantityNumericUpDown)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton BallQuantityRandomModeRadioButton;
        private System.Windows.Forms.RadioButton BallQuantityManualModeRadioButton;
        private System.Windows.Forms.Label ProgramDescriptionLabel;
        private System.Windows.Forms.Label BallQuantitySelectionModeRequestLabel;
        private System.Windows.Forms.Label BallTypesQuantityRequestLabel;
        private System.Windows.Forms.Button BallTypesQuantitySendButton;
        private System.Windows.Forms.RichTextBox ParametersInfoRichTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown BallTypesQuantityNumericUpDown;
        private System.Windows.Forms.NumericUpDown TotalBallQuantityNumericUpDown;
        private System.Windows.Forms.Button TotalBallQuantitySendButton;
        private System.Windows.Forms.Label BallDistributionRequestLabel;
        private System.Windows.Forms.RadioButton BallDistributionRandomModeRadioButton;
        private System.Windows.Forms.RadioButton BallDistributionManualModeRadioButton;
        private System.Windows.Forms.Label OneTypeBallQuantityRequestLabel;
        private System.Windows.Forms.NumericUpDown OneTypeBallQuantityNumericUpDown;
        private System.Windows.Forms.Button button1;
    }
}


 */
